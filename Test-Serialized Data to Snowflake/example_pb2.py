"""
Compiling example.proto 
"""
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x0b\x63om.example\"9\n\tMyMessage\x12\x14\n\x0cmessage_text\x18\x01 \x01(\t\x12\x16\n\x0emessage_number\x18\x02 \x01(\x05\x62\x06proto3')



_MYMESSAGE = DESCRIPTOR.message_types_by_name['MyMessage']
MyMessage = _reflection.GeneratedProtocolMessageType('MyMessage', (_message.Message,), {
  'DESCRIPTOR' : _MYMESSAGE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:com.example.MyMessage)
  })
_sym_db.RegisterMessage(MyMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MYMESSAGE._serialized_start=30
  _MYMESSAGE._serialized_end=87
# @@protoc_insertion_point(module_scope)