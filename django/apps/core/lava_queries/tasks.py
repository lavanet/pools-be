from apps.core.blockchains.constants import NetworkType
from .classes import LavaQuery


def test_show_all_chains():
    result = LavaQuery(network=NetworkType.TESTNET).query_show_all_chains()
    print('show_all_chains TESTNET:', result)
    result = LavaQuery(network=NetworkType.MAINNET).query_show_all_chains()
    print('show_all_chains MAINNET:', result)


def test_pools():
    result = LavaQuery().query_pools()
    print('test_rewards_pools:', result)


def test_providers():
    result = LavaQuery().query_providers('NEAR')
    print('test_rewards_pools:', result)


def test_iprpc_spec_rewards():
    result = LavaQuery().query_iprpc_spec_rewards(height=944001)
    print('test_iprpc_spec_rewards:', result)
    result = LavaQuery().query_iprpc_spec_rewards(height=1168000)
    print('test_iprpc_spec_rewards:', result)


def test_denom():
    result = LavaQuery().query_denom_trace('E3FCBEDDBAC500B1BAB90395C7D1E4F33D9B9ECFE82A16ED7D7D141A0152323F')
    print('test_iprpc_spec_rewards:', result)
