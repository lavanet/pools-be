# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/store/snapshots/v1/snapshot.proto
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
    'cosmos/store/snapshots/v1/snapshot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cosmos/store/snapshots/v1/snapshot.proto\x12\x19\x63osmos.store.snapshots.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x85\x01\n\x08Snapshot\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r\x12\x0e\n\x06\x63hunks\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12;\n\x08metadata\x18\x05 \x01(\x0b\x32#.cosmos.store.snapshots.v1.MetadataB\x04\xc8\xde\x1f\x00\" \n\x08Metadata\x12\x14\n\x0c\x63hunk_hashes\x18\x01 \x03(\x0c\"\xca\x02\n\x0cSnapshotItem\x12=\n\x05store\x18\x01 \x01(\x0b\x32,.cosmos.store.snapshots.v1.SnapshotStoreItemH\x00\x12\x45\n\x04iavl\x18\x02 \x01(\x0b\x32+.cosmos.store.snapshots.v1.SnapshotIAVLItemB\x08\xe2\xde\x1f\x04IAVLH\x00\x12\x45\n\textension\x18\x03 \x01(\x0b\x32\x30.cosmos.store.snapshots.v1.SnapshotExtensionMetaH\x00\x12P\n\x11\x65xtension_payload\x18\x04 \x01(\x0b\x32\x33.cosmos.store.snapshots.v1.SnapshotExtensionPayloadH\x00:\x13\xd2\xb4-\x0f\x63osmos-sdk 0.46B\x06\n\x04item\"6\n\x11SnapshotStoreItem\x12\x0c\n\x04name\x18\x01 \x01(\t:\x13\xd2\xb4-\x0f\x63osmos-sdk 0.46\"d\n\x10SnapshotIAVLItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x05:\x13\xd2\xb4-\x0f\x63osmos-sdk 0.46\"J\n\x15SnapshotExtensionMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r:\x13\xd2\xb4-\x0f\x63osmos-sdk 0.46\"@\n\x18SnapshotExtensionPayload\x12\x0f\n\x07payload\x18\x01 \x01(\x0c:\x13\xd2\xb4-\x0f\x63osmos-sdk 0.46B$Z\"cosmossdk.io/store/snapshots/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.snapshots.v1.snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\"cosmossdk.io/store/snapshots/types'
  _globals['_SNAPSHOT'].fields_by_name['metadata']._loaded_options = None
  _globals['_SNAPSHOT'].fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _globals['_SNAPSHOTITEM'].fields_by_name['iavl']._loaded_options = None
  _globals['_SNAPSHOTITEM'].fields_by_name['iavl']._serialized_options = b'\342\336\037\004IAVL'
  _globals['_SNAPSHOTITEM']._loaded_options = None
  _globals['_SNAPSHOTITEM']._serialized_options = b'\322\264-\017cosmos-sdk 0.46'
  _globals['_SNAPSHOTSTOREITEM']._loaded_options = None
  _globals['_SNAPSHOTSTOREITEM']._serialized_options = b'\322\264-\017cosmos-sdk 0.46'
  _globals['_SNAPSHOTIAVLITEM']._loaded_options = None
  _globals['_SNAPSHOTIAVLITEM']._serialized_options = b'\322\264-\017cosmos-sdk 0.46'
  _globals['_SNAPSHOTEXTENSIONMETA']._loaded_options = None
  _globals['_SNAPSHOTEXTENSIONMETA']._serialized_options = b'\322\264-\017cosmos-sdk 0.46'
  _globals['_SNAPSHOTEXTENSIONPAYLOAD']._loaded_options = None
  _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_options = b'\322\264-\017cosmos-sdk 0.46'
  _globals['_SNAPSHOT']._serialized_start=121
  _globals['_SNAPSHOT']._serialized_end=254
  _globals['_METADATA']._serialized_start=256
  _globals['_METADATA']._serialized_end=288
  _globals['_SNAPSHOTITEM']._serialized_start=291
  _globals['_SNAPSHOTITEM']._serialized_end=621
  _globals['_SNAPSHOTSTOREITEM']._serialized_start=623
  _globals['_SNAPSHOTSTOREITEM']._serialized_end=677
  _globals['_SNAPSHOTIAVLITEM']._serialized_start=679
  _globals['_SNAPSHOTIAVLITEM']._serialized_end=779
  _globals['_SNAPSHOTEXTENSIONMETA']._serialized_start=781
  _globals['_SNAPSHOTEXTENSIONMETA']._serialized_end=855
  _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_start=857
  _globals['_SNAPSHOTEXTENSIONPAYLOAD']._serialized_end=921
# @@protoc_insertion_point(module_scope)
