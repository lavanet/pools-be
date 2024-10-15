import base64
import json
from collections import namedtuple

import requests
from ibc.applications.transfer.v1 import query_pb2 as ibc_query
from lavanet.lava.pairing import query_pb2 as lava_pairing
from lavanet.lava.rewards import query_pb2 as lava_rewards
from lavanet.lava.spec import query_pb2 as lava_spec

from apps.core.blockchains.constants import NetworkType


class LavaQueryException(Exception):
    pass


class LavaQueryNoCommitAtHeight(LavaQueryException):
    pass


class LavaQueryInvalidHeight(LavaQueryException):
    pass


class LavaQueryBase:
    ERROR_RESPONSE = namedtuple('ErrorResponse', ['status_code', 'text'])(0, 'Unknown Error')
    NETWORKS = {
        NetworkType.MAINNET: 'https://lava.tendermintrpc.lava.build',
        NetworkType.TESTNET: 'https://lav1.tendermintrpc.lava.build',
    }

    def __init__(self, network=NetworkType.MAINNET):
        self.network = network
        self.id = -1

    def next_id(self):
        self.id += 1
        return self.id

    def _query(self, *args, **kwargs):
        raise NotImplementedError

    def _try_query(self, *args, **kwargs):
        # Retry request 3 times looking for status 200.
        response = self.ERROR_RESPONSE
        for i in range(3):
            response = self._query(*args, **kwargs)
            if response.status_code == 200:
                return response
        raise LavaQueryException(
            f'Unexpected status code [{response.status_code}, {response.text}]')


class LavaQuery(LavaQueryBase):
    NO_COMMIT_AT_HEIGHT = 18
    INVALID_HEIGHT = 26
    ERROR_RESPONSE = namedtuple('ErrorResponse', ['status_code', 'text'])(0, 'Unknown Error')

    def _query(self, method='abci_query', path='', data='', height=0):
        return requests.post(
            url=self.NETWORKS[self.network],
            json={
                'jsonrpc': '2.0',
                'id': self.next_id(),
                'method': method,
                'params': {
                    'data': data,
                    'height': str(height),
                    'path': path,
                    'prove': False,
                }})

    def query(self, method='abci_query', path='', data='', height=0):
        response = self._try_query(method=method, path=path, data=data, height=height)
        try:
            json_response = response.json()
        except:
            raise LavaQueryException(f'Path[{path}]: Failed to parse JSON response [{response.text}]')
        try:
            # Unpack response
            response = json_response['result']['response']
            value = response['value']
            code = response['code']
        except:
            raise LavaQueryException(f'Path[{path}]: Failed to get value from response [{json_response}]')
        if value:
            try:
                return base64.b64decode(value)
            except:
                raise LavaQueryException(f'Path[{path}]: Failed to decode value [{value}, {json_response}]')
        # Value did not decode, handle error codes.
        if code == self.NO_COMMIT_AT_HEIGHT:
            raise LavaQueryNoCommitAtHeight(f'Response[{response}]: No commit at height [{height}]')
        if code == self.INVALID_HEIGHT:
            raise LavaQueryInvalidHeight(f'Response[{response}]: Height in the future [{height}]')
        raise LavaQueryException(f'Response[{response}]: Unknown error')

    def query_show_all_chains(self):
        # lavad q spec show-all-chains --node "https://lav1.tendermintrpc.lava.build:443"
        parser = lava_spec.QueryShowAllChainsResponse()
        parser.ParseFromString(self.query(path='/lavanet.lava.spec.Query/ShowAllChains'))
        return parser

    def query_pools(self, height=0):
        # lavad q rewards pools --node "https://lav1.tendermintrpc.lava.build:443"
        parser = lava_rewards.QueryPoolsResponse()
        parser.ParseFromString(self.query(path='/lavanet.lava.rewards.Query/Pools', height=height))
        return parser

    def query_providers(self, chain_id):
        # lavad q pairing providers NEAR --node "https://lav1.tendermintrpc.lava.build:443"
        request = lava_pairing.QueryProvidersRequest()
        request.chainID = chain_id
        parser = lava_pairing.QueryProvidersResponse()
        parser.ParseFromString(self.query(path='/lavanet.lava.pairing.Query/Providers',
                                          data=request.SerializeToString().hex()))
        return parser

    def query_iprpc_spec_rewards(self, height=0):
        # lavad q rewards iprpc-spec-reward --node "https://lav1.tendermintrpc.lava.build:443"
        parser = lava_rewards.QueryIprpcSpecRewardResponse()
        parser.ParseFromString(self.query(path='/lavanet.lava.rewards.Query/IprpcSpecReward', height=height))
        return parser

    def query_denom_trace(self, denom_trace):
        # lavad q ibc-transfer denom-trace C09A0FFBA11313A32D42A58D820190E71E9D0D5AB3E841C0391EB9A623E07F4B --node "https://lav1.tendermintrpc.lava.build:443"
        # --node "https://lav1.tendermintrpc.lava.build:443"
        request = ibc_query.QueryDenomTraceRequest()
        request.hash = denom_trace
        parser = ibc_query.QueryDenomTraceResponse()
        parser.ParseFromString(self.query(path='/ibc.applications.transfer.v1.Query/DenomTrace',
                                          data=request.SerializeToString().hex()))
        return parser


class LavaEvents(LavaQueryBase):
    def _query(self, height=0):
        return requests.post(
            url=self.NETWORKS[self.network],
            json={
                'jsonrpc': '2.0',
                'id': self.next_id(),
                'method': 'block_results',
                'params': {'height': str(height)},
            })

    def query(self, height):
        response = self._try_query(height=height)
        try:
            json_response = response.json()
        except:
            raise LavaQueryException(f'Failed to parse JSON response [{response.text}]')
        try:
            return json_response['result']['txs_results']
        except:
            raise LavaQueryException(f'Failed to get value from response [{json_response}]')

    def query_lava_relay_payment(self, height):
        if txs_results := self.query(height=height):
            for tx in txs_results:
                for event in tx['events']:
                    if event['type'] == 'lava_relay_payment':
                        yield event['attributes']
