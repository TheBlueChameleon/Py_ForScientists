import functools


class LoggedFunction:
    indent = 0
    delta_indent = 2

    def __init__(self, f):
        self.f = f

        metaobjects_to_preserve = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
        for metaobject_name in metaobjects_to_preserve:
            old_metaobject = getattr(self.f, metaobject_name)
            setattr(self, metaobject_name, old_metaobject)

    def __call__(self, *args, **kwargs):
        print(" " * self.indent, "calling", self.f.__name__, "with arguments", args, kwargs)
        self.indent += self.delta_indent

        result = self.f(*args, **kwargs)

        self.indent -= self.delta_indent
        print(" " * self.indent, "returning from", self.f.__name__, "with result", result)
        return result


@LoggedFunction
def fib(N):
    if N < 0: return 0
    if N == 0: return 0
    if N == 1: return 1
    return fib(N - 1) + fib(N - 2)


@functools.cache
@LoggedFunction
def fib_cached(N):
    if N < 0: return 0
    if N == 0: return 0
    if N == 1: return 1
    return fib_cached(N - 1) + fib_cached(N - 2)


def main():
    print("### UNCACHED FIB")
    print(fib(5))
    print()

    print("### UNCACHED FIB, SECOND CALL")
    print(fib(5))
    print()

    print("### CACHED FIB")
    print(fib_cached(5))
    print()

    print("### CACHED FIB, SECOND CALL")
    print(fib_cached(5))
    print()

    print("### CACHED FIB, PRECOMPUTED INTERMEDIATE RESULT")
    print(fib_cached(4))
    print()

    print("### CACHED FIB, NON-PRECOMPUTED INTERMEDIATE RESULT")
    print(fib_cached(6))
    print()

    print("### PRESERVED METAOBJECT PROPERTIES:")
    print(fib.__name__)
    print(fib_cached.__name__)


if __name__ == '__main__':
    main()
