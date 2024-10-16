# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/spec/spec.proto
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
    'lavanet/lava/spec/spec.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from lavanet.lava.spec import api_collection_pb2 as lavanet_dot_lava_dot_spec_dot_api__collection__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1clavanet/lava/spec/spec.proto\x12\x11lavanet.lava.spec\x1a\x14gogoproto/gogo.proto\x1a&lavanet/lava/spec/api_collection.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xaa\x05\n\x04Spec\x12\r\n\x05index\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x1d\n\x15reliability_threshold\x18\x05 \x01(\r\x12 \n\x18\x64\x61ta_reliability_enabled\x18\x06 \x01(\x08\x12)\n!block_distance_for_finalized_data\x18\x07 \x01(\r\x12$\n\x1c\x62locks_in_finalization_proof\x18\x08 \x01(\r\x12\x1a\n\x12\x61verage_block_time\x18\t \x01(\x03\x12&\n\x1e\x61llowed_block_lag_for_qos_sync\x18\n \x01(\x03\x12\x1a\n\x12\x62lock_last_updated\x18\x0b \x01(\x04\x12;\n\x12min_stake_provider\x18\x0c \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12?\n\x0fproviders_types\x18\x0e \x01(\x0e\x32&.lavanet.lava.spec.Spec.ProvidersTypes\x12\x0f\n\x07imports\x18\x0f \x03(\t\x12\x39\n\x0f\x61pi_collections\x18\x10 \x03(\x0b\x32 .lavanet.lava.spec.ApiCollection\x12\x13\n\x0b\x63ontributor\x18\x11 \x03(\t\x12J\n\x16\x63ontributor_percentage\x18\x12 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x0e\n\x06shares\x18\x13 \x01(\x04\x12\x10\n\x08identity\x18\x14 \x01(\t\")\n\x0eProvidersTypes\x12\x0b\n\x07\x64ynamic\x10\x00\x12\n\n\x06static\x10\x01J\x04\x08\x03\x10\x04J\x04\x08\r\x10\x0e\x42-Z\'github.com/lavanet/lava/v2/x/spec/types\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.spec.spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/lavanet/lava/v2/x/spec/types\250\342\036\001'
  _globals['_SPEC'].fields_by_name['min_stake_provider']._loaded_options = None
  _globals['_SPEC'].fields_by_name['min_stake_provider']._serialized_options = b'\310\336\037\000'
  _globals['_SPEC'].fields_by_name['contributor_percentage']._loaded_options = None
  _globals['_SPEC'].fields_by_name['contributor_percentage']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPEC']._serialized_start=146
  _globals['_SPEC']._serialized_end=828
  _globals['_SPEC_PROVIDERSTYPES']._serialized_start=775
  _globals['_SPEC_PROVIDERSTYPES']._serialized_end=816
# @@protoc_insertion_point(module_scope)
