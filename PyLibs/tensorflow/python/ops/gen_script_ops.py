"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
"""

import collections as _collections

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2

# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library

def _py_func(input, token, Tout, name=None):
  r"""Invokes a python function to compute func(input)->output.

  This operation is considered stateful. For a stateless version, see
  PyFuncStateless.

  Args:
    input: A list of `Tensor` objects.
      List of Tensors that will provide input to the Op.
    token: A `string`.
      A token representing a registered python function in this address space.
    Tout: A list of `tf.DTypes`. Data types of the outputs from the op.
      The length of the list specifies the number of outputs.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`. The outputs from the Op.
  """
  result = _op_def_lib.apply_op("PyFunc", input=input, token=token, Tout=Tout,
                                name=name)
  return result



def _py_func_stateless(input, token, Tout, name=None):
  r"""A stateless version of PyFunc.

  Args:
    input: A list of `Tensor` objects.
    token: A `string`.
    Tout: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """
  result = _op_def_lib.apply_op("PyFuncStateless", input=input, token=token,
                                Tout=Tout, name=name)
  return result


def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib


# op {
#   name: "PyFunc"
#   input_arg {
#     name: "input"
#     type_list_attr: "Tin"
#   }
#   output_arg {
#     name: "output"
#     type_list_attr: "Tout"
#   }
#   attr {
#     name: "token"
#     type: "string"
#   }
#   attr {
#     name: "Tin"
#     type: "list(type)"
#     has_minimum: true
#   }
#   attr {
#     name: "Tout"
#     type: "list(type)"
#     has_minimum: true
#   }
#   is_stateful: true
# }
# op {
#   name: "PyFuncStateless"
#   input_arg {
#     name: "input"
#     type_list_attr: "Tin"
#   }
#   output_arg {
#     name: "output"
#     type_list_attr: "Tout"
#   }
#   attr {
#     name: "token"
#     type: "string"
#   }
#   attr {
#     name: "Tin"
#     type: "list(type)"
#     has_minimum: true
#   }
#   attr {
#     name: "Tout"
#     type: "list(type)"
#     has_minimum: true
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\ne\n\006PyFunc\022\014\n\005input2\003Tin\032\016\n\006output2\004Tout\"\017\n\005token\022\006string\"\023\n\003Tin\022\nlist(type)(\001\"\024\n\004Tout\022\nlist(type)(\001\210\001\001\nk\n\017PyFuncStateless\022\014\n\005input2\003Tin\032\016\n\006output2\004Tout\"\017\n\005token\022\006string\"\023\n\003Tin\022\nlist(type)(\001\"\024\n\004Tout\022\nlist(type)(\001")
