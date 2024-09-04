from .classes import LavaQuery


def test_show_all_chains():
    result = LavaQuery.query_show_all_chains()
    print('show_all_chains:', result)


def test_pools():
    result = LavaQuery.query_pools()
    print('test_rewards_pools:', result)


def test_providers():
    result = LavaQuery.query_providers('NEAR')
    print('test_rewards_pools:', result)


def test_iprpc_spec_rewards():
    result = LavaQuery.query_iprpc_spec_rewards()
    print('test_iprpc_spec_rewards:', result)


def test_():
    # lavad test events 1 --event lava_relay_payment --node https://lav1.tendermintrpc.lava.build:443

    """

    lavad q rewards iprpc-spec-reward --height 1600000 --node "https://lav1.tendermintrpc.lava.build:443"
    lavad q subscription estimated-rewards lava@1f8kg6htavv67x4e54j6zvlg6pwzcsg52k3wu80 NEAR --node "https://lav1.tendermintrpc.lava.build:443"
    """
    print('object:', object)

"""

lavad q rewards iprpc-spec-reward --node "https://lav1.tendermintrpc.lava.build:443"


"""