# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/orm/v1/orm.proto
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
    'cosmos/orm/v1/orm.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63osmos/orm/v1/orm.proto\x12\rcosmos.orm.v1\x1a google/protobuf/descriptor.proto\"\x8f\x01\n\x0fTableDescriptor\x12\x38\n\x0bprimary_key\x18\x01 \x01(\x0b\x32#.cosmos.orm.v1.PrimaryKeyDescriptor\x12\x36\n\x05index\x18\x02 \x03(\x0b\x32\'.cosmos.orm.v1.SecondaryIndexDescriptor\x12\n\n\x02id\x18\x03 \x01(\r\">\n\x14PrimaryKeyDescriptor\x12\x0e\n\x06\x66ields\x18\x01 \x01(\t\x12\x16\n\x0e\x61uto_increment\x18\x02 \x01(\x08\"F\n\x18SecondaryIndexDescriptor\x12\x0e\n\x06\x66ields\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0e\n\x06unique\x18\x03 \x01(\x08\"!\n\x13SingletonDescriptor\x12\n\n\x02id\x18\x01 \x01(\r:Q\n\x05table\x12\x1f.google.protobuf.MessageOptions\x18\xee\xb3\xea\x31 \x01(\x0b\x32\x1e.cosmos.orm.v1.TableDescriptor:Y\n\tsingleton\x12\x1f.google.protobuf.MessageOptions\x18\xef\xb3\xea\x31 \x01(\x0b\x32\".cosmos.orm.v1.SingletonDescriptorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.orm.v1.orm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TABLEDESCRIPTOR']._serialized_start=77
  _globals['_TABLEDESCRIPTOR']._serialized_end=220
  _globals['_PRIMARYKEYDESCRIPTOR']._serialized_start=222
  _globals['_PRIMARYKEYDESCRIPTOR']._serialized_end=284
  _globals['_SECONDARYINDEXDESCRIPTOR']._serialized_start=286
  _globals['_SECONDARYINDEXDESCRIPTOR']._serialized_end=356
  _globals['_SINGLETONDESCRIPTOR']._serialized_start=358
  _globals['_SINGLETONDESCRIPTOR']._serialized_end=391
# @@protoc_insertion_point(module_scope)
