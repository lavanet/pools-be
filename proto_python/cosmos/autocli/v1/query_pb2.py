# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/autocli/v1/query.proto
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
    'cosmos/autocli/v1/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.autocli.v1 import options_pb2 as cosmos_dot_autocli_dot_v1_dot_options__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63osmos/autocli/v1/query.proto\x12\x11\x63osmos.autocli.v1\x1a\x1f\x63osmos/autocli/v1/options.proto\x1a\x1b\x63osmos/query/v1/query.proto\"\x13\n\x11\x41ppOptionsRequest\"\xbe\x01\n\x12\x41ppOptionsResponse\x12P\n\x0emodule_options\x18\x01 \x03(\x0b\x32\x38.cosmos.autocli.v1.AppOptionsResponse.ModuleOptionsEntry\x1aV\n\x12ModuleOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .cosmos.autocli.v1.ModuleOptions:\x02\x38\x01\x32i\n\x05Query\x12`\n\nAppOptions\x12$.cosmos.autocli.v1.AppOptionsRequest\x1a%.cosmos.autocli.v1.AppOptionsResponse\"\x05\x88\xe7\xb0*\x00\x42+Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.autocli.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1'
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._loaded_options = None
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_QUERY'].methods_by_name['AppOptions']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AppOptions']._serialized_options = b'\210\347\260*\000'
  _globals['_APPOPTIONSREQUEST']._serialized_start=114
  _globals['_APPOPTIONSREQUEST']._serialized_end=133
  _globals['_APPOPTIONSRESPONSE']._serialized_start=136
  _globals['_APPOPTIONSRESPONSE']._serialized_end=326
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_start=240
  _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_end=326
  _globals['_QUERY']._serialized_start=328
  _globals['_QUERY']._serialized_end=433
# @@protoc_insertion_point(module_scope)
