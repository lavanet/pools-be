import requests

from .settings import API_KEY


class CoinGeckoException(Exception):
    pass


class CoinGeckoQuery:
    @staticmethod
    def query(endpoint, params=None):
        response = requests.get(
            url=f'https://api.coingecko.com/api/v3{endpoint}',
            headers={'x-cg-api-key': API_KEY},
            params=params, )
        if response.status_code != 200:
            raise CoinGeckoException(
                f'Path[{endpoint}]: Unexpected status code [{response.status_code}, {response.text}]')
        try:
            return response.json()
        except:
            raise CoinGeckoException(f'Path[{endpoint}]: Failed to parse JSON response [{response.text}]')

    @classmethod
    def query_coin_list(cls):
        return cls.query(endpoint=f'/coins/list')

    @classmethod
    def query_coin(cls, coin_id):
        return cls.query(endpoint=f'/coins/{coin_id}')

    @classmethod
    def query_coin_price(cls, coin_id, month, dt_format='%d-%m-%Y'):
        from apps.core.blockchains.utils import get_month
        response = cls.query(endpoint=f'/coins/{coin_id}/history',
                             params={'date': get_month(month).strftime(dt_format), })
        print('response:', response['market_data']['current_price']['usd'])
