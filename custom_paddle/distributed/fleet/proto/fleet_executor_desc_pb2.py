# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: paddle/fluid/distributed/fleet_executor/fleet_executor_desc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nApaddle/fluid/distributed/fleet_executor/fleet_executor_desc.proto\x12\x12paddle.distributed\")\n\x08RankInfo\x12\x0c\n\x04rank\x18\x01 \x02(\x03\x12\x0f\n\x07ip_port\x18\x02 \x02(\t\"\\\n\x11\x46leetExecutorDesc\x12\x13\n\x08\x63ur_rank\x18\x01 \x01(\x03:\x01\x30\x12\x32\n\x0c\x63luster_info\x18\x02 \x03(\x0b\x32\x1c.paddle.distributed.RankInfo')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'paddle.fluid.distributed.fleet_executor.fleet_executor_desc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RANKINFO._serialized_start=89
  _RANKINFO._serialized_end=130
  _FLEETEXECUTORDESC._serialized_start=132
  _FLEETEXECUTORDESC._serialized_end=224
# @@protoc_insertion_point(module_scope)
