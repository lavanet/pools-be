from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from django.utils.timezone import now


# from apps.core.coingecko.classes import CoinGeckoQuery
# from apps.core.kvstore.models import KeyValue


# def refresh_coin_list():
#     """
#     Save all known coins that start with "u" to avoid confusion with microtokens.
#     """
#     coin_list = {'date_updated': now().strftime('%Y-%m-%d %H:%M:%S'), 'coins': []}
#     for coin in CoinGeckoQuery.query_coin_list():
#         if coin['symbol'].startswith('u'):
#             coin_list['coins'].append(coin['id'])
#     KeyValue.set('coingecko_tokens_startswith_u', coin_list)
#     return coin_list
#
#
# def is_microtoken(denom):
#     denom = denom.lower()
#     if not denom.startswith('u') or denom.startswith('usd'):
#         return False
#     coingecko_tokens = KeyValue.get('coingecko_tokens_startswith_u', {})
#     try:
#         time_expire = (now() - timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S')
#         assert time_expire < coingecko_tokens['date_updated']
#     except:
#         coingecko_tokens = refresh_coin_list()
#     return denom not in coingecko_tokens['coins']


def get_month(number, month_zero=datetime(2024, 3, 17)):
    return month_zero + relativedelta(months=number)


def expire(timeout):
    if timeout:
        return now() + timedelta(seconds=timeout)
