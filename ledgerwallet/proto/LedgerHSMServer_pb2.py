# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LedgerHSMServer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='LedgerHSMServer.proto',
  package='bluehsmserver',
  syntax='proto3',
  serialized_options=_b('\n\033com.ledger.bluehsm.protobufB\014BlueHSMProtoH\001'),
  serialized_pb=_b('\n\x15LedgerHSMServer.proto\x12\rbluehsmserver\"7\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\r\n\x05local\x18\x03 \x01(\x08\"\xa1\x01\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nparameters\x18\x02 \x01(\x0c\x12\x11\n\treference\x18\x03 \x01(\t\x12\x0b\n\x03\x65lf\x18\x04 \x01(\x0c\x12\r\n\x05\x63lose\x18\x05 \x01(\x08\x12\x12\n\nlargeStack\x18\x06 \x01(\x08\x12\x33\n\x11remote_parameters\x18\x07 \x03(\x0b\x32\x18.bluehsmserver.Parameter\"L\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08response\x18\x02 \x01(\x0c\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x11\n\texception\x18\x04 \x01(\tB-\n\x1b\x63om.ledger.bluehsm.protobufB\x0c\x42lueHSMProtoH\x01\x62\x06proto3')
)




_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='bluehsmserver.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='bluehsmserver.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='bluehsmserver.Parameter.alias', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local', full_name='bluehsmserver.Parameter.local', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=40,
  serialized_end=95,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bluehsmserver.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bluehsmserver.Request.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='bluehsmserver.Request.parameters', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference', full_name='bluehsmserver.Request.reference', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elf', full_name='bluehsmserver.Request.elf', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='bluehsmserver.Request.close', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='largeStack', full_name='bluehsmserver.Request.largeStack', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_parameters', full_name='bluehsmserver.Request.remote_parameters', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=98,
  serialized_end=259,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bluehsmserver.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bluehsmserver.Response.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bluehsmserver.Response.response', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='bluehsmserver.Response.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exception', full_name='bluehsmserver.Response.exception', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=261,
  serialized_end=337,
)

_REQUEST.fields_by_name['remote_parameters'].message_type = _PARAMETER
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'LedgerHSMServer_pb2'
  # @@protoc_insertion_point(class_scope:bluehsmserver.Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'LedgerHSMServer_pb2'
  # @@protoc_insertion_point(class_scope:bluehsmserver.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'LedgerHSMServer_pb2'
  # @@protoc_insertion_point(class_scope:bluehsmserver.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
