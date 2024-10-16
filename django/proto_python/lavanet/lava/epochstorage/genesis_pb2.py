# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/epochstorage/genesis.proto
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
    'lavanet/lava/epochstorage/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from lavanet.lava.epochstorage import params_pb2 as lavanet_dot_lava_dot_epochstorage_dot_params__pb2
from lavanet.lava.epochstorage import stake_storage_pb2 as lavanet_dot_lava_dot_epochstorage_dot_stake__storage__pb2
from lavanet.lava.epochstorage import epoch_details_pb2 as lavanet_dot_lava_dot_epochstorage_dot_epoch__details__pb2
from lavanet.lava.epochstorage import fixated_params_pb2 as lavanet_dot_lava_dot_epochstorage_dot_fixated__params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'lavanet/lava/epochstorage/genesis.proto\x12\x19lavanet.lava.epochstorage\x1a\x14gogoproto/gogo.proto\x1a&lavanet/lava/epochstorage/params.proto\x1a-lavanet/lava/epochstorage/stake_storage.proto\x1a-lavanet/lava/epochstorage/epoch_details.proto\x1a.lavanet/lava/epochstorage/fixated_params.proto\"\x9a\x02\n\x0cGenesisState\x12\x37\n\x06params\x18\x01 \x01(\x0b\x32!.lavanet.lava.epochstorage.ParamsB\x04\xc8\xde\x1f\x00\x12G\n\x10stakeStorageList\x18\x02 \x03(\x0b\x32\'.lavanet.lava.epochstorage.StakeStorageB\x04\xc8\xde\x1f\x00\x12=\n\x0c\x65pochDetails\x18\x03 \x01(\x0b\x32\'.lavanet.lava.epochstorage.EpochDetails\x12I\n\x11\x66ixatedParamsList\x18\x04 \x03(\x0b\x32(.lavanet.lava.epochstorage.FixatedParamsB\x04\xc8\xde\x1f\x00\x42\x31Z/github.com/lavanet/lava/v2/x/epochstorage/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.epochstorage.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/github.com/lavanet/lava/v2/x/epochstorage/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['stakeStorageList']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['stakeStorageList']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['fixatedParamsList']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['fixatedParamsList']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=275
  _globals['_GENESISSTATE']._serialized_end=557
# @@protoc_insertion_point(module_scope)
