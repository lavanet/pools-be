# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/protocol/params.proto
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
    'lavanet/lava/protocol/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"lavanet/lava/protocol/params.proto\x12\x15lavanet.lava.protocol\x1a\x14gogoproto/gogo.proto\"\xd1\x01\n\x07Version\x12\x33\n\x0fprovider_target\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"provider_target\"\x12-\n\x0cprovider_min\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:\"provider_min\"\x12\x33\n\x0f\x63onsumer_target\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"consumer_target\"\x12-\n\x0c\x63onsumer_min\x18\x04 \x01(\tB\x17\xf2\xde\x1f\x13yaml:\"consumer_min\"\"E\n\x06Params\x12\x35\n\x07version\x18\x01 \x01(\x0b\x32\x1e.lavanet.lava.protocol.VersionB\x04\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00\x42-Z+github.com/lavanet/lava/v2/x/protocol/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.protocol.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/lavanet/lava/v2/x/protocol/types'
  _globals['_VERSION'].fields_by_name['provider_target']._loaded_options = None
  _globals['_VERSION'].fields_by_name['provider_target']._serialized_options = b'\362\336\037\026yaml:\"provider_target\"'
  _globals['_VERSION'].fields_by_name['provider_min']._loaded_options = None
  _globals['_VERSION'].fields_by_name['provider_min']._serialized_options = b'\362\336\037\023yaml:\"provider_min\"'
  _globals['_VERSION'].fields_by_name['consumer_target']._loaded_options = None
  _globals['_VERSION'].fields_by_name['consumer_target']._serialized_options = b'\362\336\037\026yaml:\"consumer_target\"'
  _globals['_VERSION'].fields_by_name['consumer_min']._loaded_options = None
  _globals['_VERSION'].fields_by_name['consumer_min']._serialized_options = b'\362\336\037\023yaml:\"consumer_min\"'
  _globals['_PARAMS'].fields_by_name['version']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['version']._serialized_options = b'\310\336\037\000'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\230\240\037\000'
  _globals['_VERSION']._serialized_start=84
  _globals['_VERSION']._serialized_end=293
  _globals['_PARAMS']._serialized_start=295
  _globals['_PARAMS']._serialized_end=364
# @@protoc_insertion_point(module_scope)
