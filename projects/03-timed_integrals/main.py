import time

import matplotlib.pyplot as plt
import numpy as np
import scipy as sci

# ==================================================================================================================== #

epsilon = np.finfo(np.float).eps

f_well_behaved = lambda x: np.exp(-x ** 2) * np.cos(x)
f_oscillating = lambda x: np.sin((x + epsilon) ** -2)
f_expensive = lambda x: sci.special.jv(0, x)

# results for \int_{-\infty}^{\infty} f(x) \dd{x}
result_well_behaved = np.sqrt(np.pi / np.sqrt(np.e))
result_oscillating = np.sqrt(2 * np.pi)
result_expensive = 2.0

# we can't actually put values from -infty .. infty to memory, so we elect a cutoff point where we assume the integrand
# to be small enough to be negligible.
finite_infty = 100

# for automated testing of all of them, create a few nice handles on the data
names = [r"\exp(-x^2) \cdot cos(x)", r"\sin((x + \varepsilon)^{-2})", r"\sin(x) / x"]
functions = {
    names[0]: f_well_behaved,
    names[1]: f_oscillating,
    names[2]: f_expensive
}
result_named = {
    names[0]: result_well_behaved,
    names[1]: result_oscillating,
    names[2]: result_expensive
}


# ==================================================================================================================== #
# helper functions and constants

def timed(f):
    def inner(*args, **kwargs):
        tic = time.perf_counter()
        result = f(*args, **kwargs)
        toc = time.perf_counter()
        return toc - tic, result

    return inner


# ==================================================================================================================== #

@timed
def prepare_data(N, f):
    xs = np.linspace(-finite_infty, finite_infty, N)
    ys = f(xs)
    return xs, ys


# .................................................................................................................... #

@timed
def int_f_quad(f):
    return sci.integrate.quad(f, -np.infty, +np.infty)


@timed
def int_f_romberg(f):
    return sci.integrate.romberg(f, -finite_infty, +finite_infty)


@timed
def int_f_gauss(f):
    return sci.integrate.quadrature(f, -finite_infty, +finite_infty)


# .................................................................................................................... #

@timed
def int_v_trapezoid(xs, ys):
    return sci.integrate.trapezoid(ys, xs)


@timed
def int_v_simpson(xs, ys):
    return sci.integrate.simpson(ys, xs)


@timed
def int_v_romberg(xs, ys):
    dx = xs[1] - xs[0]
    return sci.integrate.romb(ys, dx)


# ==================================================================================================================== #

def collect_data(series):
    """
    Integrates a function f using several methods and accuracy settings, and returns a dict with all the results for use
    by plot_data.

    :param series: The name of the test run, used only on screen while collecting results
    :return: A dict of structure key: string -> value: list
        keys describe the timing experiment and will be used as labels in plot_data.
        values have inner structure [runtime, result]
        result depends on the key:
            precomputing: [[runtimes], [values_x], [values_y]]
            quad continuous: runtime, integral, estimate accuracy
            romberg continuous: runtime, integral

    """

    f = functions[series]
    print(f"Data collection on series '{series}' started ... this could take some time...")

    # this will collect all result tables with a string key used as plot label
    # indices: results["key"][sample_size, quality_index]
    # where sample_size
    results = dict()

    # specify how many support points we will be using for the vector-based integrators
    exponent_max = 20
    Ns = np.logspace(0, exponent_max, exponent_max + 1, base=2, dtype=int) + 1

    # prepare pre-evaluated data and record time
    raw_precompute = [prepare_data(N, f) for N in Ns]
    # data_precompute = np.array([[runtime, xs, ys] for runtime, (xs, ys) in raw_precompute])
    results["precomputing"] = [[runtime, len(vectors[0])] for runtime, vectors in raw_precompute]

    # these integrators cannot (so easily) be coerced to using N support points -- treat differently from the rest
    runtime, (integral, accuracy) = int_f_quad(f)
    results["quad continuous"] = [runtime, integral, accuracy]
    results["romberg continuous"] = int_f_romberg(f)

    # # gaussian integration returns a tuple of (integral, None) -- discard the none
    # raw_gauss = [int_f_gauss_(f, N) for N in Ns]
    # data_gauss = np.array([[runtime, result[0]] for (runtime, result) in raw_gauss])
    # results["gauss continuous"] = data_gauss

    runtime, (integral, accuracy) = int_f_gauss(f)
    results["gauss continuous"] = [runtime, integral, accuracy]

    # vector based integrators
    results["trapezoid vector"] = [int_v_trapezoid(*vectors) for rt, vectors in raw_precompute]
    results["simpson vector"] = [int_v_simpson(*vectors) for rt, vectors in raw_precompute]
    results["romberg vector"] = [int_v_romberg(*vectors) for rt, vectors in raw_precompute]

    print("done.")
    return results


# .................................................................................................................... #

def plot_data(data, series):
    fig, axs = plt.subplots(2, 2)
    fig.set_size_inches(16, 16)
    fig.suptitle(f"Integration Benchmark for series '${series}$'")
    fig.subplots_adjust(wspace=0.4,
                        hspace=0.4)

    continuous_names = ["quad continuous", "romberg continuous", "gauss continuous"]
    continuous_results = [data[name] for name in continuous_names]
    continuous_times = [datapoint[0] for datapoint in continuous_results]
    continuous_errors = 100 * np.abs(
        np.array([datapoint[1] for datapoint in continuous_results]) - result_named[series]) / result_named[series]

    axs[0, 0].set_title("Runtimes continuous integrators".title())
    axs[0, 0].set_xlabel("Integrator")
    axs[0, 0].set_ylabel("Runtime in s")
    axs[0, 0].bar(continuous_names, continuous_times)

    axs[1, 0].set_title("Relative Integration Errors Continuous Integrators")
    axs[1, 0].set_xlabel("Integrator")
    axs[1, 0].set_ylabel("Error in %")
    axs[1, 0].set_ylim(0, 10)
    axs[1, 0].bar(continuous_names, continuous_errors)

    precompute_times, vector_sizes = zip(*data["precomputing"])

    vectorized_names = ["trapezoid vector", "simpson vector", "romberg vector"]
    vectorized_results = [data[name] for name in vectorized_names]
    vectorized_times = [list(zip(*result))[0] for result in vectorized_results]
    vectorized_ints = np.array([list(zip(*result))[1] for result in vectorized_results])
    vectorized_errors = np.abs(vectorized_ints - result_named[series]) / result_named[series]

    axs[0, 1].set_title("Runtimes vectorized integrators".title())
    axs[0, 1].set_xlabel("Vector length")
    axs[0, 1].set_ylabel("Runtime in s")
    axs[0, 1].set_xscale("log")
    axs[0, 1].set_yscale("log")
    for name, times in zip(vectorized_names, vectorized_times):
        axs[0, 1].plot(vector_sizes, times, label=name)
    axs[0, 1].plot(vector_sizes, precompute_times, color="grey", linewidth=0, marker=".",
                   label="precomputing vectors")
    lvl_quad = continuous_times[0]
    axs[0, 1].plot([0, vector_sizes[-1]], [lvl_quad, lvl_quad], color="red", linewidth=1, label="quad")
    axs[0, 1].legend(loc="upper left")

    axs[1, 1].set_title("Relative integration errors vectorized integrators".title())
    axs[1, 1].set_xlabel("Vector length")
    axs[1, 1].set_ylabel("Error in %")
    axs[1, 1].set_xscale("log")
    axs[1, 1].set_yscale("log")
    for name, error in zip(vectorized_names, vectorized_errors):
        axs[1, 1].plot(vector_sizes, error, label=name)
    lvl_quad = continuous_errors[0]
    axs[1, 1].plot([0, vector_sizes[-1]], [lvl_quad, lvl_quad], color="red", linewidth=1, label="quad")
    axs[1, 1].legend()

    plt.show()

    print(series)
    print("-" * 40)
    for key, value in data.items():
        print(key, value)
    print("=" * 40)
    print()


# ==================================================================================================================== #

if __name__ == '__main__':
    for name in names:
        results = collect_data(name)
        plot_data(results, name)
