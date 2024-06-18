# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sgame_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import hero_pb2 as hero__pb2
from . import scene_pb2 as scene__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sgame_state.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11sgame_state.proto\x1a\nhero.proto\x1a\x0bscene.proto\"X\n\nFrameState\x12\x0f\n\x07\x66rameNo\x18\x01 \x02(\x05\x12\x1f\n\x0bhero_states\x18\x02 \x03(\x0b\x32\n.HeroState\x12\x18\n\x07\x62ullets\x18\x03 \x03(\x0b\x32\x07.Bullet')
  ,
  dependencies=[hero__pb2.DESCRIPTOR,scene__pb2.DESCRIPTOR,])




_FRAMESTATE = _descriptor.Descriptor(
  name='FrameState',
  full_name='FrameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frameNo', full_name='FrameState.frameNo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hero_states', full_name='FrameState.hero_states', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bullets', full_name='FrameState.bullets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=134,
)

_FRAMESTATE.fields_by_name['hero_states'].message_type = hero__pb2._HEROSTATE
_FRAMESTATE.fields_by_name['bullets'].message_type = scene__pb2._BULLET
DESCRIPTOR.message_types_by_name['FrameState'] = _FRAMESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameState = _reflection.GeneratedProtocolMessageType('FrameState', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESTATE,
  __module__ = 'sgame_state_pb2'
  # @@protoc_insertion_point(class_scope:FrameState)
  ))
_sym_db.RegisterMessage(FrameState)


# @@protoc_insertion_point(module_scope)
