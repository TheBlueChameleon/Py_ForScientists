import ctypes

_lib = ctypes.CDLL("../lib/libbindingExamples.so")

class point2d_t(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double)
    ]

_functions_to_export = [
    # function name as string, tuple of parameter types, return type
    ("func_void_empty",     (), None),
    ("func_void_int",       (ctypes.c_int,), None),
    ("func_void_charPtr",   (ctypes.c_char_p,), None),
    ("func_void_doublePtr", (ctypes.POINTER(ctypes.c_double),), None),
    ("func_void_struct",    (point2d_t,), None),
    ("func_void_structPtr", (ctypes.POINTER(point2d_t),), None),

    ("func_int_empty",      (), ctypes.c_int),
    ("func_charPtr_empty",  (), ctypes.c_char_p),
]

_variables_to_export = [
    # variable name as string, data types
    ("pi", ctypes.c_double)
]

def _generate_typed_call(func, parameter_types):
    def wrapper(*args):
        typed_args = (parameter_type(arg) for arg, parameter_type in zip(args, parameter_types))
        return func(*typed_args)
    return wrapper

for funcname, parameter_types, return_type in _functions_to_export:
    func = _lib[funcname]
    func.restype = return_type
    globals()[funcname] = func

for variable, datatype in _variables_to_export:
    globals()[variable] = datatype.in_dll(_lib, variable)

