from collections import defaultdict

from django.db.models import Sum
from django.db.transaction import atomic

from apps.core.blockchains.models import Chain, Reward, RewardType
from apps.core.kvstore.models import KeyValue
from apps.core.lava_queries.classes import LavaQuery, LavaQueryException, LavaQueryInvalidHeight
from libs.utils import logger


def update_chain_list():
    result = LavaQuery().query_show_all_chains()
    for chain in result.chainInfoList:
        logger.debug('update_chain_list(): chain: %s, %s', chain.chainID, chain.chainName)
        Chain.objects.update_or_create(
            id=chain.chainID,
            defaults={'name': chain.chainName, })


def update_chain_rpc_providers():
    lavaquery = LavaQuery()
    for chain in Chain.objects.all():
        try:
            result = lavaquery.query_providers(chain.id)
            chain.rpc_node_runners = len(result.stakeEntry)
            chain.save(update_fields=['rpc_node_runners'])
            logger.debug('update_chain_rpc_providers(): chain: %s, rpc_node_runners: %s', chain, chain.rpc_node_runners)
        except LavaQueryException:
            pass


def update_chain_rewards(iteration=30):
    height = KeyValue.get('height_last_reward', 1)
    step = KeyValue.get('step_last_reward', 16000)
    current_month = KeyValue.get('current_month', 0)
    rewards = defaultdict(dict)
    denoms = {}
    lavaquery = LavaQuery()
    for i in range(iteration):
        try:
            logger.debug('update_chain_rewards(): height: %s', height)
            result = lavaquery.query_iprpc_spec_rewards(height=height)
            current_month = max(current_month, result.current_month_id)
            for reward in result.iprpc_rewards:
                for spec_fund in reward.spec_funds:
                    rewards[reward.id][spec_fund.spec] = {
                        'reward_amount': spec_fund.fund[0].amount,
                        'reward_denom': spec_fund.fund[0].denom, }
                    denoms[spec_fund.spec] = spec_fund.fund[0].denom
            logger.debug('update_chain_rewards(): months: %s', list(rewards.keys()))
        except LavaQueryInvalidHeight:
            break
        except LavaQueryException:
            pass
        except KeyboardInterrupt:
            break
        height += step
    existing_rewards = Reward.objects.values_list('chain_id', 'month')
    with atomic():
        KeyValue.set('height_last_reward', height)
        KeyValue.set('current_month', current_month)
        rewards_ = []
        for month, chains in rewards.items():
            for chain_id, chain_rewards in chains.items():
                if (chain_id, month) not in existing_rewards:
                    rewards_.append(Reward(
                        chain_id=chain_id,
                        reward_amount=chain_rewards['reward_amount'],
                        month=month,
                        reward_type=RewardType.ONCHAIN, ))
        created = Reward.objects.bulk_create(rewards_)
        logger.debug('update_chain_rewards(): Rewards created: %s', created)
    update_denoms(denoms)


def update_denoms(denoms):
    logger.debug('update_denoms(): denoms: %s', denoms)
    lavaquery = LavaQuery()
    for chain, denom in denoms.items():
        try:
            base_denom = lavaquery.query_denom_trace(denom.split('/')[-1]).denom_trace.base_denom
            Chain.objects.filter(id=chain).update(denom=base_denom)
        except LavaQueryException:
            pass


def update_chains_past_future_rewards():
    current_month = KeyValue.get('current_month')
    if not current_month:
        raise ValueError('current_month is not set')
    for chain in Chain.objects.all():
        chain.update_past_rewards(current_month)
        chain.update_future_rewards(current_month)
        chain.save(update_fields=['past_rewards', 'future_rewards'])
    update_totals()


def update_totals():
    total_past_rewards = Chain.objects.aggregate(total_past_rewards=Sum('past_rewards'))['total_past_rewards']
    total_future_rewards = Chain.objects.aggregate(total_future_rewards=Sum('future_rewards'))['total_future_rewards']
    KeyValue.set('total_past_rewards', str(total_past_rewards))
    KeyValue.set('total_future_rewards', str(total_future_rewards))
    KeyValue.set('total_rewards', str(total_past_rewards + total_future_rewards))


def daily_update():
    update_chain_list()
    update_chain_rpc_providers()

    update_chain_rewards()

    update_chains_past_future_rewards()
