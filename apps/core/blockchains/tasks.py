from apps.core.blockchains.models import Chain
from apps.core.lava_queries.classes import LavaQuery, LavaQueryParseError, LavaQueryException


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


def update_chain_rewards():
    # WIP: Testing current_month_id at different block height.
    for i in range(700000, 1800000, 4000):
        try:
            result = LavaQuery.query_iprpc_spec_rewards(height=i)
            print('result:', i, result.current_month_id)
        except LavaQueryException:
            print('result:', i, 'error')
