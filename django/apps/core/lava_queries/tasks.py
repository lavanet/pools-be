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



def test_denom():
    result = LavaQuery().query_denom_trace('E3FCBEDDBAC500B1BAB90395C7D1E4F33D9B9ECFE82A16ED7D7D141A0152323F')
    print('test_iprpc_spec_rewards:', result)


def test_requests():
    events = LavaEvents()

    events_ = list(events.query_lava_relay_payment(height=1919761))
    for event in events_:
        # print('event:', event, len(event))
        for thing in event:
            print('thing:', thing)

    return

    for i in range(2):
        height = 340780 + i
        print('height:', height, i)
        events_ = list(events.query_lava_relay_payment(height=height))
        for event in events_:
            print('event:', event, len(event))

