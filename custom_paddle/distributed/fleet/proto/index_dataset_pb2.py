# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: paddle/fluid/distributed/index_dataset/index_dataset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:paddle/fluid/distributed/index_dataset/index_dataset.proto\x12\x12paddle.distributed\"P\n\tIndexNode\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0f\n\x07is_leaf\x18\x02 \x02(\x08\x12\x13\n\x0bprobability\x18\x03 \x02(\x02\x12\x11\n\titem_name\x18\x04 \x01(\t\"*\n\x08TreeMeta\x12\x0e\n\x06height\x18\x01 \x02(\x05\x12\x0e\n\x06\x62ranch\x18\x02 \x02(\x05\"$\n\x06KVItem\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x02(\x0c')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'paddle.fluid.distributed.index_dataset.index_dataset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INDEXNODE._serialized_start=82
  _INDEXNODE._serialized_end=162
  _TREEMETA._serialized_start=164
  _TREEMETA._serialized_end=206
  _KVITEM._serialized_start=208
  _KVITEM._serialized_end=244
# @@protoc_insertion_point(module_scope)
