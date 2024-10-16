# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/base/abci/v1beta1/abci.proto
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
    'cosmos/base/abci/v1beta1/abci.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cometbft.abci.v1 import types_pb2 as cometbft_dot_abci_dot_v1_dot_types__pb2
from cometbft.types.v1 import block_pb2 as cometbft_dot_types_dot_v1_dot_block__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/base/abci/v1beta1/abci.proto\x12\x18\x63osmos.base.abci.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63ometbft/abci/v1/types.proto\x1a\x1d\x63ometbft/types/v1/block.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xfa\x02\n\nTxResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x1a\n\x06txhash\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06TxHash\x12\x11\n\tcodespace\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\t\x12\x0f\n\x07raw_log\x18\x06 \x01(\t\x12O\n\x04logs\x18\x07 \x03(\x0b\x32(.cosmos.base.abci.v1beta1.ABCIMessageLogB\x17\xc8\xde\x1f\x00\xaa\xdf\x1f\x0f\x41\x42\x43IMessageLogs\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x12\n\ngas_wanted\x18\t \x01(\x03\x12\x10\n\x08gas_used\x18\n \x01(\x03\x12 \n\x02tx\x18\x0b \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x0c \x01(\t\x12@\n\x06\x65vents\x18\r \x03(\x0b\x32\x17.cometbft.abci.v1.EventB\x17\xc8\xde\x1f\x00\xda\xb4-\x0f\x63osmos-sdk 0.45:\x04\x88\xa0\x1f\x00\"\x92\x01\n\x0e\x41\x42\x43IMessageLog\x12 \n\tmsg_index\x18\x01 \x01(\rB\r\xea\xde\x1f\tmsg_index\x12\x0b\n\x03log\x18\x02 \x01(\t\x12K\n\x06\x65vents\x18\x03 \x03(\x0b\x32%.cosmos.base.abci.v1beta1.StringEventB\x14\xc8\xde\x1f\x00\xaa\xdf\x1f\x0cStringEvents:\x04\x80\xdc \x01\"`\n\x0bStringEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12=\n\nattributes\x18\x02 \x03(\x0b\x32#.cosmos.base.abci.v1beta1.AttributeB\x04\xc8\xde\x1f\x00:\x04\x80\xdc \x01\"\'\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"/\n\x07GasInfo\x12\x12\n\ngas_wanted\x18\x01 \x01(\x04\x12\x10\n\x08gas_used\x18\x02 \x01(\x04\"\x9e\x01\n\x06Result\x12\x10\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42\x02\x18\x01\x12\x0b\n\x03log\x18\x02 \x01(\t\x12-\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x17.cometbft.abci.v1.EventB\x04\xc8\xde\x1f\x00\x12@\n\rmsg_responses\x18\x04 \x03(\x0b\x32\x14.google.protobuf.AnyB\x13\xda\xb4-\x0f\x63osmos-sdk 0.46:\x04\x88\xa0\x1f\x00\"\x85\x01\n\x12SimulationResponse\x12=\n\x08gas_info\x18\x01 \x01(\x0b\x32!.cosmos.base.abci.v1beta1.GasInfoB\x08\xc8\xde\x1f\x00\xd0\xde\x1f\x01\x12\x30\n\x06result\x18\x02 \x01(\x0b\x32 .cosmos.base.abci.v1beta1.Result\"1\n\x07MsgData\x12\x10\n\x08msg_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c:\x06\x18\x01\x80\xdc \x01\"\x88\x01\n\tTxMsgData\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.cosmos.base.abci.v1beta1.MsgDataB\x02\x18\x01\x12@\n\rmsg_responses\x18\x02 \x03(\x0b\x32\x14.google.protobuf.AnyB\x13\xda\xb4-\x0f\x63osmos-sdk 0.46:\x04\x80\xdc \x01\"\xa6\x01\n\x0fSearchTxsResult\x12\x13\n\x0btotal_count\x18\x01 \x01(\x04\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x12\x13\n\x0bpage_number\x18\x03 \x01(\x04\x12\x12\n\npage_total\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x31\n\x03txs\x18\x06 \x03(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse:\x04\x80\xdc \x01\"\xa0\x01\n\x12SearchBlocksResult\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x13\n\x0bpage_number\x18\x03 \x01(\x03\x12\x12\n\npage_total\x18\x04 \x01(\x03\x12\r\n\x05limit\x18\x05 \x01(\x03\x12(\n\x06\x62locks\x18\x06 \x03(\x0b\x32\x18.cometbft.types.v1.Block:\x04\x80\xdc \x01\x42(Z\"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.abci.v1beta1.abci_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\"github.com/cosmos/cosmos-sdk/types\330\341\036\000'
  _globals['_TXRESPONSE'].fields_by_name['txhash']._loaded_options = None
  _globals['_TXRESPONSE'].fields_by_name['txhash']._serialized_options = b'\342\336\037\006TxHash'
  _globals['_TXRESPONSE'].fields_by_name['logs']._loaded_options = None
  _globals['_TXRESPONSE'].fields_by_name['logs']._serialized_options = b'\310\336\037\000\252\337\037\017ABCIMessageLogs'
  _globals['_TXRESPONSE'].fields_by_name['events']._loaded_options = None
  _globals['_TXRESPONSE'].fields_by_name['events']._serialized_options = b'\310\336\037\000\332\264-\017cosmos-sdk 0.45'
  _globals['_TXRESPONSE']._loaded_options = None
  _globals['_TXRESPONSE']._serialized_options = b'\210\240\037\000'
  _globals['_ABCIMESSAGELOG'].fields_by_name['msg_index']._loaded_options = None
  _globals['_ABCIMESSAGELOG'].fields_by_name['msg_index']._serialized_options = b'\352\336\037\tmsg_index'
  _globals['_ABCIMESSAGELOG'].fields_by_name['events']._loaded_options = None
  _globals['_ABCIMESSAGELOG'].fields_by_name['events']._serialized_options = b'\310\336\037\000\252\337\037\014StringEvents'
  _globals['_ABCIMESSAGELOG']._loaded_options = None
  _globals['_ABCIMESSAGELOG']._serialized_options = b'\200\334 \001'
  _globals['_STRINGEVENT'].fields_by_name['attributes']._loaded_options = None
  _globals['_STRINGEVENT'].fields_by_name['attributes']._serialized_options = b'\310\336\037\000'
  _globals['_STRINGEVENT']._loaded_options = None
  _globals['_STRINGEVENT']._serialized_options = b'\200\334 \001'
  _globals['_RESULT'].fields_by_name['data']._loaded_options = None
  _globals['_RESULT'].fields_by_name['data']._serialized_options = b'\030\001'
  _globals['_RESULT'].fields_by_name['events']._loaded_options = None
  _globals['_RESULT'].fields_by_name['events']._serialized_options = b'\310\336\037\000'
  _globals['_RESULT'].fields_by_name['msg_responses']._loaded_options = None
  _globals['_RESULT'].fields_by_name['msg_responses']._serialized_options = b'\332\264-\017cosmos-sdk 0.46'
  _globals['_RESULT']._loaded_options = None
  _globals['_RESULT']._serialized_options = b'\210\240\037\000'
  _globals['_SIMULATIONRESPONSE'].fields_by_name['gas_info']._loaded_options = None
  _globals['_SIMULATIONRESPONSE'].fields_by_name['gas_info']._serialized_options = b'\310\336\037\000\320\336\037\001'
  _globals['_MSGDATA']._loaded_options = None
  _globals['_MSGDATA']._serialized_options = b'\030\001\200\334 \001'
  _globals['_TXMSGDATA'].fields_by_name['data']._loaded_options = None
  _globals['_TXMSGDATA'].fields_by_name['data']._serialized_options = b'\030\001'
  _globals['_TXMSGDATA'].fields_by_name['msg_responses']._loaded_options = None
  _globals['_TXMSGDATA'].fields_by_name['msg_responses']._serialized_options = b'\332\264-\017cosmos-sdk 0.46'
  _globals['_TXMSGDATA']._loaded_options = None
  _globals['_TXMSGDATA']._serialized_options = b'\200\334 \001'
  _globals['_SEARCHTXSRESULT']._loaded_options = None
  _globals['_SEARCHTXSRESULT']._serialized_options = b'\200\334 \001'
  _globals['_SEARCHBLOCKSRESULT']._loaded_options = None
  _globals['_SEARCHBLOCKSRESULT']._serialized_options = b'\200\334 \001'
  _globals['_TXRESPONSE']._serialized_start=203
  _globals['_TXRESPONSE']._serialized_end=581
  _globals['_ABCIMESSAGELOG']._serialized_start=584
  _globals['_ABCIMESSAGELOG']._serialized_end=730
  _globals['_STRINGEVENT']._serialized_start=732
  _globals['_STRINGEVENT']._serialized_end=828
  _globals['_ATTRIBUTE']._serialized_start=830
  _globals['_ATTRIBUTE']._serialized_end=869
  _globals['_GASINFO']._serialized_start=871
  _globals['_GASINFO']._serialized_end=918
  _globals['_RESULT']._serialized_start=921
  _globals['_RESULT']._serialized_end=1079
  _globals['_SIMULATIONRESPONSE']._serialized_start=1082
  _globals['_SIMULATIONRESPONSE']._serialized_end=1215
  _globals['_MSGDATA']._serialized_start=1217
  _globals['_MSGDATA']._serialized_end=1266
  _globals['_TXMSGDATA']._serialized_start=1269
  _globals['_TXMSGDATA']._serialized_end=1405
  _globals['_SEARCHTXSRESULT']._serialized_start=1408
  _globals['_SEARCHTXSRESULT']._serialized_end=1574
  _globals['_SEARCHBLOCKSRESULT']._serialized_start=1577
  _globals['_SEARCHBLOCKSRESULT']._serialized_end=1737
# @@protoc_insertion_point(module_scope)
