# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/pairing/params.proto
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
    'lavanet/lava/pairing/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!lavanet/lava/pairing/params.proto\x12\x14lavanet.lava.pairing\x1a\x14gogoproto/gogo.proto\"\xd4\x02\n\x06Params\x12;\n\x12\x65pochBlocksOverlap\x18\x08 \x01(\x04\x42\x1f\xf2\xde\x1f\x1byaml:\"epoch_blocks_overlap\"\x12\x63\n\tQoSWeight\x18\r \x01(\tBP\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1eyaml:\"data_reliability_reward\"\x12`\n#recommendedEpochNumToCollectPayment\x18\x0e \x01(\x04\x42\x33\xf2\xde\x1f/yaml:\"recommended_epoch_num_to_collect_payment\":\x04\x98\xa0\x1f\x00J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rB,Z*github.com/lavanet/lava/v2/x/pairing/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.pairing.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*github.com/lavanet/lava/v2/x/pairing/types'
  _globals['_PARAMS'].fields_by_name['epochBlocksOverlap']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['epochBlocksOverlap']._serialized_options = b'\362\336\037\033yaml:\"epoch_blocks_overlap\"'
  _globals['_PARAMS'].fields_by_name['QoSWeight']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['QoSWeight']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\036yaml:\"data_reliability_reward\"'
  _globals['_PARAMS'].fields_by_name['recommendedEpochNumToCollectPayment']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['recommendedEpochNumToCollectPayment']._serialized_options = b'\362\336\037/yaml:\"recommended_epoch_num_to_collect_payment\"'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\230\240\037\000'
  _globals['_PARAMS']._serialized_start=82
  _globals['_PARAMS']._serialized_end=422
# @@protoc_insertion_point(module_scope)
