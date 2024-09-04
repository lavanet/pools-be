# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/store/v1beta1/listening.proto
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
    'cosmos/store/v1beta1/listening.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cometbft.abci.v1 import types_pb2 as cometbft_dot_abci_dot_v1_dot_types__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/store/v1beta1/listening.proto\x12\x14\x63osmos.store.v1beta1\x1a\x1c\x63ometbft/abci/v1/types.proto\x1a\x19\x63osmos_proto/cosmos.proto\"a\n\x0bStoreKVPair\x12\x11\n\tstore_key\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x02 \x01(\x08\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\r\n\x05value\x18\x04 \x01(\x0c:\x13\xd2\xb4-\x0f\x63osmos-sdk 0.43\"\xfa\x01\n\rBlockMetadata\x12\x39\n\x0fresponse_commit\x18\x06 \x01(\x0b\x32 .cometbft.abci.v1.CommitResponse\x12\x46\n\x16request_finalize_block\x18\x07 \x01(\x0b\x32&.cometbft.abci.v1.FinalizeBlockRequest\x12H\n\x17response_finalize_block\x18\x08 \x01(\x0b\x32\'.cometbft.abci.v1.FinalizeBlockResponseJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\x42\x1aZ\x18\x63osmossdk.io/store/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.v1beta1.listening_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cosmossdk.io/store/types'
  _globals['_STOREKVPAIR']._loaded_options = None
  _globals['_STOREKVPAIR']._serialized_options = b'\322\264-\017cosmos-sdk 0.43'
  _globals['_STOREKVPAIR']._serialized_start=119
  _globals['_STOREKVPAIR']._serialized_end=216
  _globals['_BLOCKMETADATA']._serialized_start=219
  _globals['_BLOCKMETADATA']._serialized_end=469
# @@protoc_insertion_point(module_scope)
