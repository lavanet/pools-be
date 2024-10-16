# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: lavanet/lava/spec/query.proto
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
    'lavanet/lava/spec/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from lavanet.lava.spec import params_pb2 as lavanet_dot_lava_dot_spec_dot_params__pb2
from lavanet.lava.spec import spec_pb2 as lavanet_dot_lava_dot_spec_dot_spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dlavanet/lava/spec/query.proto\x12\x11lavanet.lava.spec\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1elavanet/lava/spec/params.proto\x1a\x1clavanet/lava/spec/spec.proto\"\x14\n\x12QueryParamsRequest\"F\n\x13QueryParamsResponse\x12/\n\x06params\x18\x01 \x01(\x0b\x32\x19.lavanet.lava.spec.ParamsB\x04\xc8\xde\x1f\x00\"&\n\x13QueryGetSpecRequest\x12\x0f\n\x07\x43hainID\x18\x01 \x01(\t\"C\n\x14QueryGetSpecResponse\x12+\n\x04Spec\x18\x01 \x01(\x0b\x32\x17.lavanet.lava.spec.SpecB\x04\xc8\xde\x1f\x00\"Q\n\x13QueryAllSpecRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x80\x01\n\x14QueryAllSpecResponse\x12+\n\x04Spec\x18\x01 \x03(\x0b\x32\x17.lavanet.lava.spec.SpecB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1b\n\x19QueryShowAllChainsRequest\"e\n\x1aQueryShowAllChainsResponse\x12\x41\n\rchainInfoList\x18\x02 \x03(\x0b\x32*.lavanet.lava.spec.ShowAllChainsInfoStructJ\x04\x08\x01\x10\x02\"n\n\x17ShowAllChainsInfoStruct\x12\x11\n\tchainName\x18\x01 \x01(\t\x12\x0f\n\x07\x63hainID\x18\x02 \x01(\t\x12\x1c\n\x14\x65nabledApiInterfaces\x18\x03 \x03(\t\x12\x11\n\tapi_count\x18\x04 \x01(\x04\".\n\x19QueryShowChainInfoRequest\x12\x11\n\tchainName\x18\x01 \x01(\t\"B\n\x07\x41piList\x12\x11\n\tinterface\x18\x04 \x01(\t\x12\x15\n\rsupportedApis\x18\x05 \x03(\t\x12\r\n\x05\x61\x64\x64on\x18\x06 \x01(\t\"\x9e\x01\n\x1aQueryShowChainInfoResponse\x12\x0f\n\x07\x63hainID\x18\x01 \x01(\t\x12\x12\n\ninterfaces\x18\x02 \x03(\t\x12>\n\x1asupportedApisInterfaceList\x18\x03 \x03(\x0b\x32\x1a.lavanet.lava.spec.ApiList\x12\x1b\n\x13optional_interfaces\x18\x04 \x03(\t2\xd8\x07\n\x05Query\x12z\n\x06Params\x12%.lavanet.lava.spec.QueryParamsRequest\x1a&.lavanet.lava.spec.QueryParamsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/lavanet/lava/spec/params\x12\x82\x01\n\x04Spec\x12&.lavanet.lava.spec.QueryGetSpecRequest\x1a\'.lavanet.lava.spec.QueryGetSpecResponse\")\x82\xd3\xe4\x93\x02#\x12!/lavanet/lava/spec/spec/{ChainID}\x12{\n\x07SpecAll\x12&.lavanet.lava.spec.QueryAllSpecRequest\x1a\'.lavanet.lava.spec.QueryAllSpecResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/lavanet/lava/spec/spec\x12\x89\x01\n\x07SpecRaw\x12&.lavanet.lava.spec.QueryGetSpecRequest\x1a\'.lavanet.lava.spec.QueryGetSpecResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/lavanet/lava/spec/spec_raw/{ChainID}\x12\x82\x01\n\nSpecAllRaw\x12&.lavanet.lava.spec.QueryAllSpecRequest\x1a\'.lavanet.lava.spec.QueryAllSpecResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/lavanet/lava/spec/spec_raw\x12\x98\x01\n\rShowAllChains\x12,.lavanet.lava.spec.QueryShowAllChainsRequest\x1a-.lavanet.lava.spec.QueryShowAllChainsResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/lavanet/lava/spec/show_all_chains\x12\xa4\x01\n\rShowChainInfo\x12,.lavanet.lava.spec.QueryShowChainInfoRequest\x1a-.lavanet.lava.spec.QueryShowChainInfoResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./lavanet/lava/spec/show_chain_info/{chainName}B)Z\'github.com/lavanet/lava/v2/x/spec/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lavanet.lava.spec.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/lavanet/lava/v2/x/spec/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYGETSPECRESPONSE'].fields_by_name['Spec']._loaded_options = None
  _globals['_QUERYGETSPECRESPONSE'].fields_by_name['Spec']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLSPECRESPONSE'].fields_by_name['Spec']._loaded_options = None
  _globals['_QUERYALLSPECRESPONSE'].fields_by_name['Spec']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\033\022\031/lavanet/lava/spec/params'
  _globals['_QUERY'].methods_by_name['Spec']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Spec']._serialized_options = b'\202\323\344\223\002#\022!/lavanet/lava/spec/spec/{ChainID}'
  _globals['_QUERY'].methods_by_name['SpecAll']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SpecAll']._serialized_options = b'\202\323\344\223\002\031\022\027/lavanet/lava/spec/spec'
  _globals['_QUERY'].methods_by_name['SpecRaw']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SpecRaw']._serialized_options = b'\202\323\344\223\002\'\022%/lavanet/lava/spec/spec_raw/{ChainID}'
  _globals['_QUERY'].methods_by_name['SpecAllRaw']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SpecAllRaw']._serialized_options = b'\202\323\344\223\002\035\022\033/lavanet/lava/spec/spec_raw'
  _globals['_QUERY'].methods_by_name['ShowAllChains']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ShowAllChains']._serialized_options = b'\202\323\344\223\002$\022\"/lavanet/lava/spec/show_all_chains'
  _globals['_QUERY'].methods_by_name['ShowChainInfo']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ShowChainInfo']._serialized_options = b'\202\323\344\223\0020\022./lavanet/lava/spec/show_chain_info/{chainName}'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=210
  _globals['_QUERYPARAMSREQUEST']._serialized_end=230
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=232
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=302
  _globals['_QUERYGETSPECREQUEST']._serialized_start=304
  _globals['_QUERYGETSPECREQUEST']._serialized_end=342
  _globals['_QUERYGETSPECRESPONSE']._serialized_start=344
  _globals['_QUERYGETSPECRESPONSE']._serialized_end=411
  _globals['_QUERYALLSPECREQUEST']._serialized_start=413
  _globals['_QUERYALLSPECREQUEST']._serialized_end=494
  _globals['_QUERYALLSPECRESPONSE']._serialized_start=497
  _globals['_QUERYALLSPECRESPONSE']._serialized_end=625
  _globals['_QUERYSHOWALLCHAINSREQUEST']._serialized_start=627
  _globals['_QUERYSHOWALLCHAINSREQUEST']._serialized_end=654
  _globals['_QUERYSHOWALLCHAINSRESPONSE']._serialized_start=656
  _globals['_QUERYSHOWALLCHAINSRESPONSE']._serialized_end=757
  _globals['_SHOWALLCHAINSINFOSTRUCT']._serialized_start=759
  _globals['_SHOWALLCHAINSINFOSTRUCT']._serialized_end=869
  _globals['_QUERYSHOWCHAININFOREQUEST']._serialized_start=871
  _globals['_QUERYSHOWCHAININFOREQUEST']._serialized_end=917
  _globals['_APILIST']._serialized_start=919
  _globals['_APILIST']._serialized_end=985
  _globals['_QUERYSHOWCHAININFORESPONSE']._serialized_start=988
  _globals['_QUERYSHOWCHAININFORESPONSE']._serialized_end=1146
  _globals['_QUERY']._serialized_start=1149
  _globals['_QUERY']._serialized_end=2133
# @@protoc_insertion_point(module_scope)
