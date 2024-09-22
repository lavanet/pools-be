from .classes import LavaQuery, LavaEvents


def test_show_all_chains():
    result = LavaQuery().query_show_all_chains()
    print('show_all_chains:', result)


def test_pools():
    result = LavaQuery().query_pools()
    print('test_rewards_pools:', result)


def test_providers():
    result = LavaQuery().query_providers('NEAR')
    print('test_rewards_pools:', result)


def test_iprpc_spec_rewards():
    result = LavaQuery().query_iprpc_spec_rewards()
    print('test_iprpc_spec_rewards:', result)


def test_requests():
    events = LavaEvents()

    for i in range(6):
        height = 340778 + i
        print('height:', height, i)
        for event in events.query_lava_relay_payment(height=height):
            print('event:', event)
