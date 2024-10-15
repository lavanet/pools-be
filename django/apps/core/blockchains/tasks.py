from collections import defaultdict

from django.db.models import Sum, Max
from django.db.transaction import atomic
from django.utils.timezone import now

from apps.core.blockchains.classes import DenomStore
from apps.core.blockchains.constants import NetworkType
from apps.core.blockchains.models import Chain, Reward, RewardType, BlockRequest
from apps.core.blockchains.utils import expire
from apps.core.kvstore.models import KeyValue
from apps.core.lava_queries.classes import LavaQuery, LavaQueryException, LavaQueryInvalidHeight, LavaEvents
from libs.print_time import PrintTime
from libs.utils import logger


def update_chain_list():
    for network in NetworkType:
        result = LavaQuery(network=network).query_show_all_chains()
        for chain in result.chainInfoList:
            logger.debug('update_chain_list(): %s, %s, %s', network, chain.chainID, chain.chainName)
            Chain.objects.update_or_create(
                chain_id=chain.chainID,
                defaults={'name': chain.chainName, })


def update_chain_coingecko():
    for chain in Chain.objects.filter(network=NetworkType.MAINNET).exclude(coingecko_id=None):
        print('chain', chain)
        chain.update_coingecko_price()


def update_chain_rpc_providers():
    for chain in Chain.objects.all():
        chain.update_chain_rpc_providers()


def update_chain_rewards(iteration=30, network=NetworkType.MAINNET):
    """
    Use maximum iteration to avoid lambda timeout of 60 seconds.
    """
    height = KeyValue.get(f'{network}_height_last_reward', 1)
    step = KeyValue.get(f'{network}_step_last_reward', 16000)
    lavaquery = LavaQuery(network=network)
    chains = {c[1]: c[0] for c in Chain.objects.values_list('id', 'chain_id')}
    denom_store = DenomStore()

    def _query_height(_height):
        logger.debug('update_chain_rewards(): height: %s', _height)
        result = lavaquery.query_iprpc_spec_rewards(height=_height)
        for reward in result.iprpc_rewards:
            for spec_fund in reward.spec_funds:
                reward_, created = Reward.objects.update_or_create(
                    chain_id=chains[spec_fund.spec],
                    month=reward.id,
                    reward_type=RewardType.ONCHAIN,
                    denom=denom_store.get(spec_fund.fund[0].denom),
                    defaults={'reward_amount': spec_fund.fund[0].amount})
                if created:
                    logger.debug('update_chain_rewards(): created: %s, month: %s', reward_, result.current_month_id)
        return result.current_month_id

    for i in range(iteration):
        try:
            _query_height(height)
        except LavaQueryInvalidHeight:
            break
        except LavaQueryException:
            pass
        except KeyboardInterrupt:
            break
        height += step
    current_month = _query_height(0)
    with atomic():
        KeyValue.set(f'{network}_height_last_reward', height)
        KeyValue.set(f'{network}_current_month', current_month)


def update_chains_past_future_rewards(network=NetworkType.MAINNET):
    current_month = KeyValue.get(f'{network}_current_month')
    if current_month is None:
        raise ValueError('current_month is not set')
    for chain in Chain.objects.all():
        chain.update_rewards(current_month, commit=False)
        chain.update_months_remaining(current_month)
        chain.save(update_fields=['past_rewards', 'future_rewards', 'rewards_per_month', 'months_remaining'])
    update_total_rewards()


def update_total_rewards():
    chains = Chain.objects.filter()
    total_past_rewards = chains.aggregate(total_past_rewards=Sum('past_rewards'))['total_past_rewards']
    total_future_rewards = chains.aggregate(total_future_rewards=Sum('future_rewards'))['total_future_rewards']
    KeyValue.set(f'total_past_rewards', str(total_past_rewards))
    KeyValue.set(f'total_future_rewards', str(total_future_rewards))
    KeyValue.set(f'total_rewards', str(total_past_rewards + total_future_rewards))


def update_request_relays(network, timeout=None):
    chains = {chain.chain_id: chain.pk for chain in Chain.objects.all()}
    expire_time = expire(timeout)

    def get_relays(event):
        for entry in event:
            chain_id = None
            relayNumber = None
            for e in entry:
                if e['key'].startswith('chainID.'):
                    chain_id = e['value']
                if e['key'].startswith('relayNumber.'):
                    relayNumber = e['value']
            if chain_id and relayNumber:
                yield chain_id, relayNumber

    events = LavaEvents(network=network)
    height = KeyValue.get(f'{network}_relay_height', 0)

    while not expire_time or now() < expire_time:
        height += 1
        relays = defaultdict(int)
        try:
            for chainid, relaynumber in get_relays(events.query_lava_relay_payment(height=height)):
                relays[chainid] += int(relaynumber)
            logger.debug('update_request_relays() relays: %s, %s', relays, height)

            blockrequest = []
            for chainid, relaynumber in relays.items():
                blockrequest.append(BlockRequest(
                    chain_id=chains[chainid],
                    height=height,
                    network=network,
                    requests=relaynumber))
            BlockRequest.objects.bulk_create(blockrequest)
        except:
            break
    KeyValue.set(f'{network}_relay_height', height)


def update_request_relays_testnet():
    update_request_relays(NetworkType.TESTNET, timeout=50)


def update_request_relays_mainnet():
    update_request_relays(NetworkType.MAINNET, timeout=50)


def update_total_requests():
    for chain in Chain.objects.all():
        chain.update_total_requests()
    total_requests = Chain.objects.aggregate(total_requests=Sum('total_requests'))['total_requests'] or 0
    KeyValue.set('total_requests', total_requests)


@PrintTime()
def hourly_update():
    update_chain_list()
    update_chain_rewards()
    update_chains_past_future_rewards()
    update_total_rewards()
    update_total_requests()


def test_update_total_rewards():
    chain = Chain.objects.get(pk='ETH1')
    print('before:', chain.past_rewards, chain.future_rewards, chain.total_rewards)
    update_total_rewards()
    print('after:', chain.past_rewards, chain.future_rewards, chain.total_rewards)


def test_manual():
    chain = Chain.objects.get(pk=92)
    print('chain:', chain)
    chain.update_future_rewards(6)


def test_microtoken():
    from apps.core.blockchains.utils import is_microtoken

    tokens = ['usdt', 'ulava', 'uarch', 'uatom', 'uniwswap', 'uwon', 'uusdt']
    for token in tokens:
        print(token, is_microtoken(token))
