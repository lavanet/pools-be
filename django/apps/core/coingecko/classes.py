import requests

from .settings import API_KEY


class CoinGeckoException(Exception):
    pass


class CoinGeckoQuery:
    @staticmethod
    def query(endpoint):
        response = requests.get(
            url=f'https://api.coingecko.com/api/v3{endpoint}',
            headers={'x-cg-api-key': API_KEY}, )
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
