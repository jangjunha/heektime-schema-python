# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heektime-schema/period.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='heektime-schema/period.proto',
  package='heek.heektime',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cheektime-schema/period.proto\x12\rheek.heektime\"<\n\x06Period\x12\x0e\n\x06period\x18\x01 \x01(\x05\x12\x11\n\ttimeBegin\x18\x02 \x01(\x05\x12\x0f\n\x07timeEnd\x18\x03 \x01(\x05\x62\x06proto3'
)




_PERIOD = _descriptor.Descriptor(
  name='Period',
  full_name='heek.heektime.Period',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='period', full_name='heek.heektime.Period.period', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeBegin', full_name='heek.heektime.Period.timeBegin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeEnd', full_name='heek.heektime.Period.timeEnd', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Period'] = _PERIOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Period = _reflection.GeneratedProtocolMessageType('Period', (_message.Message,), {
  'DESCRIPTOR' : _PERIOD,
  '__module__' : 'heektime_schema.period_pb2'
  # @@protoc_insertion_point(class_scope:heek.heektime.Period)
  })
_sym_db.RegisterMessage(Period)


# @@protoc_insertion_point(module_scope)
