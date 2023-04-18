import functools
import time

import matplotlib.pyplot as plt
import numpy as np

args = list(range(0, 34, 1))


# ==================================================================================================================== #

def timed(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        tic = time.perf_counter()
        result = f(*args, **kwargs)
        toc = time.perf_counter()
        return result, toc - tic

    return inner


def fib(N):
    if N < 0: return 0
    if N == 0: return 0
    if N == 1: return 1
    return fib(N - 1) + fib(N - 2)


@functools.cache
def fib_cached(N):
    if N < 0: return 0
    if N == 0: return 0
    if N == 1: return 1
    return fib_cached(N - 1) + fib_cached(N - 2)


# ==================================================================================================================== #

def main():
    simple_fib = timed(fib)
    pseudo_cached_fib = timed(functools.cache(fib))
    correctly_cached_fib = timed(fib_cached)

    funcs = [simple_fib, pseudo_cached_fib, pseudo_cached_fib, correctly_cached_fib, correctly_cached_fib]
    labels = ["simple", "pseudo-cached (1st exec.)", "pseudo-cached (2nd exec.)", "properly cached (1st exec.)",
              "properly cached (2nd exec.)"]
    times = np.zeros(shape=(len(args), len(funcs)), dtype=np.float)

    print("... collecting data ... this may take a while ...")
    for i, N in enumerate(args):
        print("   at N =", N)
        for j, f in enumerate(funcs):
            result, runtime = f(N)
            times[i, j] = runtime
    print("done.")
    print()

    # ................................................................................................................ #
    # print results

    print(" Runtimes")
    print("~~~~~~~~~~")

    width_col_1 = 10
    width_others = 27

    print(f"{'argument':^{width_col_1}}|", end="")
    for label in labels:
        print(f"{label:^{width_others}}|", end="")
    print()

    print("-" * width_col_1 + "+", end="")
    print(("-" * width_others + "+") * len(labels))

    format_string = "|".join(f"{{{i}:^{width_others}.4E}}" for i, lbl in enumerate(labels))
    for line in zip(args, times):
        print(f"{line[0]:^{width_col_1}}|", end="")
        print(format_string.format(*line[1]) + "|")

    # ................................................................................................................ #
    # plot results

    plt.plot(args, times, label=labels)
    plt.title("Runtimes of Fibonacci-Implementations")
    plt.xlabel("Argument")
    plt.ylabel("Runtime")
    plt.yscale("log")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
