from collections import defaultdict
from pprint import pprint

from apps.core.blockchains.models import Chain, Reward
from apps.core.lava_queries.classes import LavaQuery, LavaQueryException


def update_chain_list():
    result = LavaQuery.query_show_all_chains()
    for chain in result.chainInfoList:
        print('chain:', chain.chainName)
        print('chain:', chain.chainID)

        Chain.objects.update_or_create(
            id=chain.chainID,
            defaults={
                'name': chain.chainName,
            })
        # tODO import logo from coingecko


def update_chain_rpc_providers():
    for chain in Chain.objects.all():
        result = LavaQuery.query_providers(chain.id)
        chain.rpc_node_runners = len(result.stakeEntry)
        chain.save(update_fields=['rpc_node_runners'])


def update_chain_rewards_1():
    result = LavaQuery.query_iprpc_spec_rewards(height=i)
    print('result:', i, result.current_month_id)
    rewards = defaultdict(dict)
    for reward in result.iprpc_rewards:
        for spec_fund in reward.spec_funds:
            rewards[spec_fund.spec][reward.id] = {
                'reward_amount': spec_fund.fund[0].amount,
                'reward_denom': spec_fund.fund[0].denom,
            }
    pprint(rewards)


def update_chain_rewards():
    # WIP: Testing current_month_id at different block height.
    for i in range(1, 1852000, 1000):
        try:
            result = LavaQuery.query_iprpc_spec_rewards(height=i)
            print('result:', i, result.current_month_id)
        except LavaQueryException:
            print('result:', i, 'error')

# block resutls from every block
# command to get events
