# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tendermint/crypto/proof.proto
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
    'tendermint/crypto/proof.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/crypto/proof.proto\x12\x11tendermint.crypto\x1a\x14gogoproto/gogo.proto\"G\n\x05Proof\x12\r\n\x05total\x18\x01 \x01(\x03\x12\r\n\x05index\x18\x02 \x01(\x03\x12\x11\n\tleaf_hash\x18\x03 \x01(\x0c\x12\r\n\x05\x61unts\x18\x04 \x03(\x0c\"?\n\x07ValueOp\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\'\n\x05proof\x18\x02 \x01(\x0b\x32\x18.tendermint.crypto.Proof\"6\n\x08\x44ominoOp\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05input\x18\x02 \x01(\t\x12\x0e\n\x06output\x18\x03 \x01(\t\"2\n\x07ProofOp\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"9\n\x08ProofOps\x12-\n\x03ops\x18\x01 \x03(\x0b\x32\x1a.tendermint.crypto.ProofOpB\x04\xc8\xde\x1f\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.crypto.proof_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PROOFOPS'].fields_by_name['ops']._loaded_options = None
  _globals['_PROOFOPS'].fields_by_name['ops']._serialized_options = b'\310\336\037\000'
  _globals['_PROOF']._serialized_start=74
  _globals['_PROOF']._serialized_end=145
  _globals['_VALUEOP']._serialized_start=147
  _globals['_VALUEOP']._serialized_end=210
  _globals['_DOMINOOP']._serialized_start=212
  _globals['_DOMINOOP']._serialized_end=266
  _globals['_PROOFOP']._serialized_start=268
  _globals['_PROOFOP']._serialized_end=318
  _globals['_PROOFOPS']._serialized_start=320
  _globals['_PROOFOPS']._serialized_end=377
# @@protoc_insertion_point(module_scope)
