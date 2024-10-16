# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/pairing/badges.proto
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
    'lavanet/lava/pairing/badges.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lavanet.lava.pairing import relay_pb2 as lavanet_dot_lava_dot_pairing_dot_relay__pb2
from lavanet.lava.pairing import query_pb2 as lavanet_dot_lava_dot_pairing_dot_query__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from lavanet.lava.epochstorage import stake_entry_pb2 as lavanet_dot_lava_dot_epochstorage_dot_stake__entry__pb2
from lavanet.lava.spec import spec_pb2 as lavanet_dot_lava_dot_spec_dot_spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!lavanet/lava/pairing/badges.proto\x12\x14lavanet.lava.pairing\x1a lavanet/lava/pairing/relay.proto\x1a lavanet/lava/pairing/query.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a+lavanet/lava/epochstorage/stake_entry.proto\x1a\x1clavanet/lava/spec/spec.proto\"X\n\x14GenerateBadgeRequest\x12\x15\n\rbadge_address\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x15\n\x07spec_id\x18\x03 \x01(\tB\x04\xc8\xde\x1f\x01\"\xd5\x01\n\x15GenerateBadgeResponse\x12*\n\x05\x62\x61\x64ge\x18\x01 \x01(\x0b\x32\x1b.lavanet.lava.pairing.Badge\x12K\n\x14get_pairing_response\x18\x02 \x01(\x0b\x32-.lavanet.lava.pairing.QueryGetPairingResponse\x12\x1c\n\x14\x62\x61\x64ge_signer_address\x18\x03 \x01(\t\x12%\n\x04spec\x18\x04 \x01(\x0b\x32\x17.lavanet.lava.spec.Spec2|\n\x0e\x42\x61\x64geGenerator\x12j\n\rGenerateBadge\x12*.lavanet.lava.pairing.GenerateBadgeRequest\x1a+.lavanet.lava.pairing.GenerateBadgeResponse\"\x00\x42,Z*github.com/lavanet/lava/v2/x/pairing/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.pairing.badges_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*github.com/lavanet/lava/v2/x/pairing/types'
  _globals['_GENERATEBADGEREQUEST'].fields_by_name['spec_id']._loaded_options = None
  _globals['_GENERATEBADGEREQUEST'].fields_by_name['spec_id']._serialized_options = b'\310\336\037\001'
  _globals['_GENERATEBADGEREQUEST']._serialized_start=256
  _globals['_GENERATEBADGEREQUEST']._serialized_end=344
  _globals['_GENERATEBADGERESPONSE']._serialized_start=347
  _globals['_GENERATEBADGERESPONSE']._serialized_end=560
  _globals['_BADGEGENERATOR']._serialized_start=562
  _globals['_BADGEGENERATOR']._serialized_end=686
# @@protoc_insertion_point(module_scope)
