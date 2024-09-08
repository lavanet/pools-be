import base64

import requests
from lavanet.lava.pairing import query_pb2 as lava_pairing
from lavanet.lava.rewards import query_pb2 as lava_rewards
from lavanet.lava.spec import query_pb2 as lava_spec


class LavaQueryException(Exception):
    pass


class LavaQueryParseError(LavaQueryException):
    pass


class LavaQuery:
    @staticmethod
    def query(method='abci_query', path='', data='', height=0):
        response = requests.post(
            url='https://lav1.tendermintrpc.lava.build',
            json={
                'jsonrpc': '2.0',
                'id': 0,
                'method': method,
                'params': {
                    'data': data,
                    'height': str(height),
                    'path': path,
                    'prove': False,
                }})
        if response.status_code != 200:
            raise LavaQueryException(
                f'Path[{path}]: Unexpected status code [{response.status_code}, {response.text}]')
        try:
            json_response = response.json()
        except:
            raise LavaQueryException(f'Path[{path}]: Failed to parse JSON response [{response.text}]')
        try:
            value = json_response['result']['response']['value']
        except:
            raise LavaQueryException(f'Path[{path}]: Failed to get value from response [{json_response}]')
        try:
            decoded = base64.b64decode(value)
        except:
            raise LavaQueryException(f'Path[{path}]: Failed to decode value [{value}, {json_response}]')
        return decoded

    @classmethod
    def query_show_all_chains(cls):
        # lavad q spec show-all-chains --node "https://lav1.tendermintrpc.lava.build:443"
        parser = lava_spec.QueryShowAllChainsResponse()
        parser.ParseFromString(cls.query(path='/lavanet.lava.spec.Query/ShowAllChains'))
        return parser

    @classmethod
    def query_pools(cls, height=0):
        # avad q rewards pools --node "https://lav1.tendermintrpc.lava.build:443"
        parser = lava_rewards.QueryPoolsResponse()
        parser.ParseFromString(cls.query(path='/lavanet.lava.rewards.Query/Pools', height=height))
        return parser

    @classmethod
    def query_providers(cls, chain_id):
        # lavad q pairing providers NEAR --node "https://lav1.tendermintrpc.lava.build:443"
        request = lava_pairing.QueryProvidersRequest()
        request.chainID = chain_id
        parser = lava_pairing.QueryProvidersResponse()
        try:
            parser.ParseFromString(cls.query(path='/lavanet.lava.pairing.Query/Providers',
                                         data=request.SerializeToString().hex()))
        except:
            raise LavaQueryParseError()
        return parser

    @classmethod
    def query_iprpc_spec_rewards(cls, height=0):
        # lavad q rewards iprpc-spec-reward --node "https://lav1.tendermintrpc.lava.build:443"
        parser = lava_rewards.QueryIprpcSpecRewardResponse()
        parser.ParseFromString(cls.query(path='/lavanet.lava.rewards.Query/IprpcSpecReward', height=height))
        return parser

# lavad q spec show-spec ETH1 --node "https://lav1.tendermintrpc.lava.build:443"
