# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: google/api/servicecontrol/v1/http_request.proto
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
    'google/api/servicecontrol/v1/http_request.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/api/servicecontrol/v1/http_request.proto\x12\x1cgoogle.api.servicecontrol.v1\x1a\x1egoogle/protobuf/duration.proto\"\xef\x02\n\x0bHttpRequest\x12\x16\n\x0erequest_method\x18\x01 \x01(\t\x12\x13\n\x0brequest_url\x18\x02 \x01(\t\x12\x14\n\x0crequest_size\x18\x03 \x01(\x03\x12\x0e\n\x06status\x18\x04 \x01(\x05\x12\x15\n\rresponse_size\x18\x05 \x01(\x03\x12\x12\n\nuser_agent\x18\x06 \x01(\t\x12\x11\n\tremote_ip\x18\x07 \x01(\t\x12\x11\n\tserver_ip\x18\r \x01(\t\x12\x0f\n\x07referer\x18\x08 \x01(\t\x12*\n\x07latency\x18\x0e \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x14\n\x0c\x63\x61\x63he_lookup\x18\x0b \x01(\x08\x12\x11\n\tcache_hit\x18\t \x01(\x08\x12*\n\"cache_validated_with_origin_server\x18\n \x01(\x08\x12\x18\n\x10\x63\x61\x63he_fill_bytes\x18\x0c \x01(\x03\x12\x10\n\x08protocol\x18\x0f \x01(\tB\xe8\x01\n com.google.api.servicecontrol.v1B\x10HttpRequestProtoP\x01ZJcloud.google.com/go/servicecontrol/apiv1/servicecontrolpb;servicecontrolpb\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.servicecontrol.v1.http_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.google.api.servicecontrol.v1B\020HttpRequestProtoP\001ZJcloud.google.com/go/servicecontrol/apiv1/servicecontrolpb;servicecontrolpb\252\002\036Google.Cloud.ServiceControl.V1\312\002\036Google\\Cloud\\ServiceControl\\V1\352\002!Google::Cloud::ServiceControl::V1'
  _globals['_HTTPREQUEST']._serialized_start=114
  _globals['_HTTPREQUEST']._serialized_end=481
# @@protoc_insertion_point(module_scope)
