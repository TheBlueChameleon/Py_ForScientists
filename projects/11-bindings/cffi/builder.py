import cffi
import pathlib

ffi = cffi.FFI()

lib_source_dir = pathlib.Path("../lib").absolute()

header_filename = lib_source_dir / "bindingExamples.h"
with open(header_filename) as h_file:
    ffi.cdef(h_file.read())

ffi.set_source(
    "bindingExamples",
    f'#include "{lib_source_dir}/bindingExamples.h"',
    libraries=[lib_source_dir / "bindingExamples"],
    library_dirs=[lib_source_dir.as_posix()],
    extra_link_args=[f"-Wl,-rpath,{lib_source_dir}"],
)

ffi.compile()