# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/rewards/query.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'lavanet/lava/rewards/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from lavanet.lava.rewards import base_pay_pb2 as lavanet_dot_lava_dot_rewards_dot_base__pay__pb2
from lavanet.lava.rewards import iprpc_pb2 as lavanet_dot_lava_dot_rewards_dot_iprpc__pb2
from lavanet.lava.rewards import params_pb2 as lavanet_dot_lava_dot_rewards_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n lavanet/lava/rewards/query.proto\x12\x14lavanet.lava.rewards\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a#lavanet/lava/rewards/base_pay.proto\x1a lavanet/lava/rewards/iprpc.proto\x1a!lavanet/lava/rewards/params.proto\"\x14\n\x12QueryParamsRequest\"I\n\x13QueryParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.lavanet.lava.rewards.ParamsB\x04\xc8\xde\x1f\x00\"\x13\n\x11QueryPoolsRequest\"v\n\x08PoolInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\\\n\x07\x62\x61lance\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\xaa\x01\n\x12QueryPoolsResponse\x12\x33\n\x05pools\x18\x01 \x03(\x0b\x32\x1e.lavanet.lava.rewards.PoolInfoB\x04\xc8\xde\x1f\x00\x12\x16\n\x0etime_to_refill\x18\x02 \x01(\x03\x12\"\n\x1a\x65stimated_blocks_to_refill\x18\x03 \x01(\x03\x12#\n\x1b\x61llocation_pool_months_left\x18\x04 \x01(\x03\"\x19\n\x17QueryBlockRewardRequest\"K\n\x18QueryBlockRewardResponse\x12/\n\x06reward\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x1b\n\x19QueryShowIprpcDataRequest\"l\n\x1aQueryShowIprpcDataResponse\x12\x31\n\x08min_cost\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13iprpc_subscriptions\x18\x02 \x03(\t\"A\n\x1bQuerySpecTrackedInfoRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\"Z\n\x1cQuerySpecTrackedInfoResponse\x12:\n\x04info\x18\x01 \x03(\x0b\x32&.lavanet.lava.rewards.BasePayWithIndexB\x04\xc8\xde\x1f\x00\"=\n)QueryIprpcProviderRewardEstimationRequest\x12\x10\n\x08provider\x18\x01 \x01(\t\"f\n*QueryIprpcProviderRewardEstimationResponse\x12\x38\n\nspec_funds\x18\x01 \x03(\x0b\x32\x1e.lavanet.lava.rewards.SpecfundB\x04\xc8\xde\x1f\x00\"+\n\x1bQueryIprpcSpecRewardRequest\x12\x0c\n\x04spec\x18\x01 \x01(\t\"x\n\x1cQueryIprpcSpecRewardResponse\x12>\n\riprpc_rewards\x18\x01 \x03(\x0b\x32!.lavanet.lava.rewards.IprpcRewardB\x04\xc8\xde\x1f\x00\x12\x18\n\x10\x63urrent_month_id\x18\x02 \x01(\x04\x32\xa5\t\n\x05Query\x12\x83\x01\n\x06Params\x12(.lavanet.lava.rewards.QueryParamsRequest\x1a).lavanet.lava.rewards.QueryParamsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/lavanet/lava/rewards/params\x12\x7f\n\x05Pools\x12\'.lavanet.lava.rewards.QueryPoolsRequest\x1a(.lavanet.lava.rewards.QueryPoolsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/lavanet/lava/rewards/pools\x12\x98\x01\n\x0b\x42lockReward\x12-.lavanet.lava.rewards.QueryBlockRewardRequest\x1a..lavanet.lava.rewards.QueryBlockRewardResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/lavanet/lava/rewards/block_reward\x12\xa1\x01\n\rShowIprpcData\x12/.lavanet.lava.rewards.QueryShowIprpcDataRequest\x1a\x30.lavanet.lava.rewards.QueryShowIprpcDataResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/lavanet/lava/rewards/show_iprpc_data\x12\xbd\x01\n\x0fSpecTrackedInfo\x12\x31.lavanet.lava.rewards.QuerySpecTrackedInfoRequest\x1a\x32.lavanet.lava.rewards.QuerySpecTrackedInfoResponse\"C\x82\xd3\xe4\x93\x02=\x12;/lavanet/lava/rewards/SpecTrackedInfo/{chain_id}/{provider}\x12\xe2\x01\n\x1dIprpcProviderRewardEstimation\x12?.lavanet.lava.rewards.QueryIprpcProviderRewardEstimationRequest\x1a@.lavanet.lava.rewards.QueryIprpcProviderRewardEstimationResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/lavanet/lava/rewards/iprpc_provider_reward/{provider}\x12\xb0\x01\n\x0fIprpcSpecReward\x12\x31.lavanet.lava.rewards.QueryIprpcSpecRewardRequest\x1a\x32.lavanet.lava.rewards.QueryIprpcSpecRewardResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./lavanet/lava/rewards/iprpc_spec_reward/{spec}B,Z*github.com/lavanet/lava/v2/x/rewards/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.rewards.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*github.com/lavanet/lava/v2/x/rewards/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_POOLINFO'].fields_by_name['balance']._loaded_options = None
  _globals['_POOLINFO'].fields_by_name['balance']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_QUERYPOOLSRESPONSE'].fields_by_name['pools']._loaded_options = None
  _globals['_QUERYPOOLSRESPONSE'].fields_by_name['pools']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYBLOCKREWARDRESPONSE'].fields_by_name['reward']._loaded_options = None
  _globals['_QUERYBLOCKREWARDRESPONSE'].fields_by_name['reward']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYSHOWIPRPCDATARESPONSE'].fields_by_name['min_cost']._loaded_options = None
  _globals['_QUERYSHOWIPRPCDATARESPONSE'].fields_by_name['min_cost']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYSPECTRACKEDINFORESPONSE'].fields_by_name['info']._loaded_options = None
  _globals['_QUERYSPECTRACKEDINFORESPONSE'].fields_by_name['info']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYIPRPCPROVIDERREWARDESTIMATIONRESPONSE'].fields_by_name['spec_funds']._loaded_options = None
  _globals['_QUERYIPRPCPROVIDERREWARDESTIMATIONRESPONSE'].fields_by_name['spec_funds']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYIPRPCSPECREWARDRESPONSE'].fields_by_name['iprpc_rewards']._loaded_options = None
  _globals['_QUERYIPRPCSPECREWARDRESPONSE'].fields_by_name['iprpc_rewards']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\036\022\034/lavanet/lava/rewards/params'
  _globals['_QUERY'].methods_by_name['Pools']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Pools']._serialized_options = b'\202\323\344\223\002\035\022\033/lavanet/lava/rewards/pools'
  _globals['_QUERY'].methods_by_name['BlockReward']._loaded_options = None
  _globals['_QUERY'].methods_by_name['BlockReward']._serialized_options = b'\202\323\344\223\002$\022\"/lavanet/lava/rewards/block_reward'
  _globals['_QUERY'].methods_by_name['ShowIprpcData']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ShowIprpcData']._serialized_options = b'\202\323\344\223\002\'\022%/lavanet/lava/rewards/show_iprpc_data'
  _globals['_QUERY'].methods_by_name['SpecTrackedInfo']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SpecTrackedInfo']._serialized_options = b'\202\323\344\223\002=\022;/lavanet/lava/rewards/SpecTrackedInfo/{chain_id}/{provider}'
  _globals['_QUERY'].methods_by_name['IprpcProviderRewardEstimation']._loaded_options = None
  _globals['_QUERY'].methods_by_name['IprpcProviderRewardEstimation']._serialized_options = b'\202\323\344\223\0028\0226/lavanet/lava/rewards/iprpc_provider_reward/{provider}'
  _globals['_QUERY'].methods_by_name['IprpcSpecReward']._loaded_options = None
  _globals['_QUERY'].methods_by_name['IprpcSpecReward']._serialized_options = b'\202\323\344\223\0020\022./lavanet/lava/rewards/iprpc_spec_reward/{spec}'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=292
  _globals['_QUERYPARAMSREQUEST']._serialized_end=312
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=314
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=387
  _globals['_QUERYPOOLSREQUEST']._serialized_start=389
  _globals['_QUERYPOOLSREQUEST']._serialized_end=408
  _globals['_POOLINFO']._serialized_start=410
  _globals['_POOLINFO']._serialized_end=528
  _globals['_QUERYPOOLSRESPONSE']._serialized_start=531
  _globals['_QUERYPOOLSRESPONSE']._serialized_end=701
  _globals['_QUERYBLOCKREWARDREQUEST']._serialized_start=703
  _globals['_QUERYBLOCKREWARDREQUEST']._serialized_end=728
  _globals['_QUERYBLOCKREWARDRESPONSE']._serialized_start=730
  _globals['_QUERYBLOCKREWARDRESPONSE']._serialized_end=805
  _globals['_QUERYSHOWIPRPCDATAREQUEST']._serialized_start=807
  _globals['_QUERYSHOWIPRPCDATAREQUEST']._serialized_end=834
  _globals['_QUERYSHOWIPRPCDATARESPONSE']._serialized_start=836
  _globals['_QUERYSHOWIPRPCDATARESPONSE']._serialized_end=944
  _globals['_QUERYSPECTRACKEDINFOREQUEST']._serialized_start=946
  _globals['_QUERYSPECTRACKEDINFOREQUEST']._serialized_end=1011
  _globals['_QUERYSPECTRACKEDINFORESPONSE']._serialized_start=1013
  _globals['_QUERYSPECTRACKEDINFORESPONSE']._serialized_end=1103
  _globals['_QUERYIPRPCPROVIDERREWARDESTIMATIONREQUEST']._serialized_start=1105
  _globals['_QUERYIPRPCPROVIDERREWARDESTIMATIONREQUEST']._serialized_end=1166
  _globals['_QUERYIPRPCPROVIDERREWARDESTIMATIONRESPONSE']._serialized_start=1168
  _globals['_QUERYIPRPCPROVIDERREWARDESTIMATIONRESPONSE']._serialized_end=1270
  _globals['_QUERYIPRPCSPECREWARDREQUEST']._serialized_start=1272
  _globals['_QUERYIPRPCSPECREWARDREQUEST']._serialized_end=1315
  _globals['_QUERYIPRPCSPECREWARDRESPONSE']._serialized_start=1317
  _globals['_QUERYIPRPCSPECREWARDRESPONSE']._serialized_end=1437
  _globals['_QUERY']._serialized_start=1440
  _globals['_QUERY']._serialized_end=2629
# @@protoc_insertion_point(module_scope)
