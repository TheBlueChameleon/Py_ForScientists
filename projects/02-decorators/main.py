import lifetime
import wrapper_functions
import pretty_logged_fib
import timed_fib
import ordered_complex
import partials

if __name__ == '__main__':
    lifetime.main()
    wrapper_functions.main()
    pretty_logged_fib.main()
    timed_fib.main()
    ordered_complex.main()
    partials.main()

# useful decorators to check out:
# functools.cache (shown in timed_fib)
# functools.wraps (used in timed_fib, discussed in an upcoming lecture on metaprogramming)
# staticmethod (builtin decorator)
# property (builtin decorator)
# atexit.register
# dataclasses.dataclass
# we can discuss them in detail if you want
