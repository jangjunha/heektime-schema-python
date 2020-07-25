# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heektime-schema/lecture.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='heektime-schema/lecture.proto',
  package='heek.heektime',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dheektime-schema/lecture.proto\x12\rheek.heektime\"\xd0\x03\n\x07Lecture\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tprofessor\x18\x03 \x01(\t\x12\x0e\n\x06\x63redit\x18\x04 \x01(\x01\x12\x16\n\x0ehours_per_week\x18\x05 \x01(\x01\x12\x10\n\x08\x63\x61tegory\x18\x06 \x03(\t\x12\x10\n\x08subtitle\x18\x07 \x01(\t\x12\x17\n\x0f\x63urriculum_type\x18\x08 \x01(\t\x12\x31\n\x05times\x18\t \x03(\x0b\x32\".heek.heektime.Lecture.LectureTime\x12*\n\x05metas\x18\n \x03(\x0b\x32\x1b.heek.heektime.Lecture.Meta\x1aV\n\x0bLectureTime\x12\x0f\n\x07weekday\x18\x01 \x01(\x05\x12\x11\n\ttimeBegin\x18\x02 \x01(\x05\x12\x0f\n\x07timeEnd\x18\x03 \x01(\x05\x12\x0c\n\x04room\x18\x06 \x01(\tJ\x04\x08\x04\x10\x06\x1at\n\x04Meta\x12\r\n\x03tag\x18\x01 \x01(\tH\x00\x12\x30\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32 .heek.heektime.Lecture.Meta.DataH\x00\x1a\"\n\x04\x44\x61ta\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\x07\n\x05valueb\x06proto3'
)




_LECTURE_LECTURETIME = _descriptor.Descriptor(
  name='LectureTime',
  full_name='heek.heektime.Lecture.LectureTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='weekday', full_name='heek.heektime.Lecture.LectureTime.weekday', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeBegin', full_name='heek.heektime.Lecture.LectureTime.timeBegin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeEnd', full_name='heek.heektime.Lecture.LectureTime.timeEnd', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room', full_name='heek.heektime.Lecture.LectureTime.room', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=309,
  serialized_end=395,
)

_LECTURE_META_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='heek.heektime.Lecture.Meta.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='heek.heektime.Lecture.Meta.Data.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='heek.heektime.Lecture.Meta.Data.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=470,
  serialized_end=504,
)

_LECTURE_META = _descriptor.Descriptor(
  name='Meta',
  full_name='heek.heektime.Lecture.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='heek.heektime.Lecture.Meta.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='heek.heektime.Lecture.Meta.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LECTURE_META_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='heek.heektime.Lecture.Meta.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=397,
  serialized_end=513,
)

_LECTURE = _descriptor.Descriptor(
  name='Lecture',
  full_name='heek.heektime.Lecture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='heek.heektime.Lecture.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='heek.heektime.Lecture.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='professor', full_name='heek.heektime.Lecture.professor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='credit', full_name='heek.heektime.Lecture.credit', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hours_per_week', full_name='heek.heektime.Lecture.hours_per_week', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='heek.heektime.Lecture.category', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='heek.heektime.Lecture.subtitle', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curriculum_type', full_name='heek.heektime.Lecture.curriculum_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='times', full_name='heek.heektime.Lecture.times', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metas', full_name='heek.heektime.Lecture.metas', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LECTURE_LECTURETIME, _LECTURE_META, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=513,
)

_LECTURE_LECTURETIME.containing_type = _LECTURE
_LECTURE_META_DATA.containing_type = _LECTURE_META
_LECTURE_META.fields_by_name['data'].message_type = _LECTURE_META_DATA
_LECTURE_META.containing_type = _LECTURE
_LECTURE_META.oneofs_by_name['value'].fields.append(
  _LECTURE_META.fields_by_name['tag'])
_LECTURE_META.fields_by_name['tag'].containing_oneof = _LECTURE_META.oneofs_by_name['value']
_LECTURE_META.oneofs_by_name['value'].fields.append(
  _LECTURE_META.fields_by_name['data'])
_LECTURE_META.fields_by_name['data'].containing_oneof = _LECTURE_META.oneofs_by_name['value']
_LECTURE.fields_by_name['times'].message_type = _LECTURE_LECTURETIME
_LECTURE.fields_by_name['metas'].message_type = _LECTURE_META
DESCRIPTOR.message_types_by_name['Lecture'] = _LECTURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lecture = _reflection.GeneratedProtocolMessageType('Lecture', (_message.Message,), {

  'LectureTime' : _reflection.GeneratedProtocolMessageType('LectureTime', (_message.Message,), {
    'DESCRIPTOR' : _LECTURE_LECTURETIME,
    '__module__' : 'heektime_schema.lecture_pb2'
    # @@protoc_insertion_point(class_scope:heek.heektime.Lecture.LectureTime)
    })
  ,

  'Meta' : _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), {

    'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
      'DESCRIPTOR' : _LECTURE_META_DATA,
      '__module__' : 'heektime_schema.lecture_pb2'
      # @@protoc_insertion_point(class_scope:heek.heektime.Lecture.Meta.Data)
      })
    ,
    'DESCRIPTOR' : _LECTURE_META,
    '__module__' : 'heektime_schema.lecture_pb2'
    # @@protoc_insertion_point(class_scope:heek.heektime.Lecture.Meta)
    })
  ,
  'DESCRIPTOR' : _LECTURE,
  '__module__' : 'heektime_schema.lecture_pb2'
  # @@protoc_insertion_point(class_scope:heek.heektime.Lecture)
  })
_sym_db.RegisterMessage(Lecture)
_sym_db.RegisterMessage(Lecture.LectureTime)
_sym_db.RegisterMessage(Lecture.Meta)
_sym_db.RegisterMessage(Lecture.Meta.Data)


# @@protoc_insertion_point(module_scope)
