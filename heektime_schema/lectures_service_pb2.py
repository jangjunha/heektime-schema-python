# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heektime-schema/lectures_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from heektime_schema import lecture_pb2 as heektime__schema_dot_lecture__pb2
from heektime_schema import period_pb2 as heektime__schema_dot_period__pb2
from heektime_schema import semester_pb2 as heektime__schema_dot_semester__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='heektime-schema/lectures_service.proto',
  package='heek.heektime',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&heektime-schema/lectures_service.proto\x12\rheek.heektime\x1a\x1dheektime-schema/lecture.proto\x1a\x1cheektime-schema/period.proto\x1a\x1eheektime-schema/semester.proto\"u\n\x12GetLecturesPayload\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12)\n\x08semester\x18\x02 \x01(\x0e\x32\x17.heek.heektime.Semester\x12&\n\x07periods\x18\x03 \x03(\x0b\x32\x15.heek.heektime.Period2_\n\x0fLecturesService\x12L\n\x0bGetLectures\x12!.heek.heektime.GetLecturesPayload\x1a\x16.heek.heektime.Lecture\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[heektime__schema_dot_lecture__pb2.DESCRIPTOR,heektime__schema_dot_period__pb2.DESCRIPTOR,heektime__schema_dot_semester__pb2.DESCRIPTOR,])




_GETLECTURESPAYLOAD = _descriptor.Descriptor(
  name='GetLecturesPayload',
  full_name='heek.heektime.GetLecturesPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='heek.heektime.GetLecturesPayload.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semester', full_name='heek.heektime.GetLecturesPayload.semester', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='periods', full_name='heek.heektime.GetLecturesPayload.periods', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=150,
  serialized_end=267,
)

_GETLECTURESPAYLOAD.fields_by_name['semester'].enum_type = heektime__schema_dot_semester__pb2._SEMESTER
_GETLECTURESPAYLOAD.fields_by_name['periods'].message_type = heektime__schema_dot_period__pb2._PERIOD
DESCRIPTOR.message_types_by_name['GetLecturesPayload'] = _GETLECTURESPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetLecturesPayload = _reflection.GeneratedProtocolMessageType('GetLecturesPayload', (_message.Message,), {
  'DESCRIPTOR' : _GETLECTURESPAYLOAD,
  '__module__' : 'heektime_schema.lectures_service_pb2'
  # @@protoc_insertion_point(class_scope:heek.heektime.GetLecturesPayload)
  })
_sym_db.RegisterMessage(GetLecturesPayload)



_LECTURESSERVICE = _descriptor.ServiceDescriptor(
  name='LecturesService',
  full_name='heek.heektime.LecturesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=269,
  serialized_end=364,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLectures',
    full_name='heek.heektime.LecturesService.GetLectures',
    index=0,
    containing_service=None,
    input_type=_GETLECTURESPAYLOAD,
    output_type=heektime__schema_dot_lecture__pb2._LECTURE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LECTURESSERVICE)

DESCRIPTOR.services_by_name['LecturesService'] = _LECTURESSERVICE

# @@protoc_insertion_point(module_scope)
