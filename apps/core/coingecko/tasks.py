from pprint import pprint

from .classes import CoinGeckoQuery


def test_list():
    result = CoinGeckoQuery.query_coin_list()
    for coin in result:
        if 'lava' in coin['id']:
            print('coin:', coin)


def test_single():
    result = CoinGeckoQuery.query_coin(coin_id='lava-network')
    print('result:', result)
    pprint(result)


def show_lava():

    print(lava['description']['en'])
    print(lava['image']['large'])
    print(lava['image']['small'])
    print(lava['image']['thumb'])
    print(lava['links']['homepage'][0])
