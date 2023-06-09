import bindingExamples
import ctypes
import struct
import numpy

type_double = ctypes.c_double
type_double_ptr = ctypes.POINTER(type_double)

param_double = type_double(8)
struct_ptr = struct.pack("d", 2.71828)

print("IMPORTED OBJECT:")
print(bindingExamples)
print()

print("EXAMPLE CALLS:")
result = bindingExamples.lib.func_charPtr_empty()
print(result)

result = bindingExamples.lib.func_void_charPtr(b"foo bar")
print(result)

bindingExamples.lib.func_void_int(8)
print()

print("EXAMPLE CONSTANT:")
print(bindingExamples.lib.pi)
print()

print("ALL KNOWN OBJECTS IN THE MODULE:")
for foreign_object in dir(bindingExamples.lib):
    print(" ", foreign_object)

print("'", bindingExamples.lib.func_void_charPtr.__doc__, "'", sep="")