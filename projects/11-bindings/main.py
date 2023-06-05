import ctypes

import numpy as np
import struct
import array

import bindingExamples


def main():
    numpy_data = np.array([np.pi, 1337], dtype=np.float64)
    point = bindingExamples.point2d_t(x=np.pi, y=1337)
    array_data = array.array("d", [2.71828])
    struct_ptr = struct.pack("d", 2.71828)

    # short names for data types
    type_double_ptr = ctypes.POINTER(ctypes.c_double)
    type_point_ptr = ctypes.POINTER(bindingExamples.point2d_t)

    bindingExamples.func_void_empty()

    bindingExamples.func_void_int(-1)
    bindingExamples.func_void_int(ctypes.c_int(-1))
    bindingExamples.func_void_int(ctypes.c_uint(-1))    # type cast does not change bit pattern. => C-lib still treats it as signed => -1
    bindingExamples.func_void_int(ctypes.c_float(-1))   # as always, messy type casts lead to undefined behaviour

    bindingExamples.func_void_charPtr("hello world".encode(encoding="ascii"))
    bindingExamples.func_void_charPtr("hello world")    # Python's internal multibyte encoding adds extra null chars => only "h" arrives in C library

    bindingExamples.func_void_doublePtr(array_data.tobytes())
    bindingExamples.func_void_doublePtr(struct_ptr)
    bindingExamples.func_void_doublePtr(ctypes.pointer(point))
    bindingExamples.func_void_doublePtr(numpy_data.ctypes.data_as(type_double_ptr))

    bindingExamples.func_void_struct(point)

    bindingExamples.func_void_structPtr(numpy_data.ctypes.data_as(type_point_ptr))
    bindingExamples.func_void_structPtr(struct.pack("dd", np.pi, 2.71828))

    print()

    print(bindingExamples.func_int_empty())
    print(bindingExamples.func_charPtr_empty().decode(encoding="ascii"))
    print(bindingExamples.func_charPtr_empty())


if __name__ == '__main__':
    main()
