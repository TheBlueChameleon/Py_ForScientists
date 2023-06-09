import time

import numpy as np
from scipy import integrate as scInt

# ==================================================================================================================== #
# test function and correct result

N_sum = int(1E+6)
data_sum = [i for i in range(N_sum)]
correct_sum = lambda N: N * (N - 1) // 2

upper_bound_integral = np.pi
dt = 1E-5
integrand = lambda x: np.sin(x)
correct_integral = lambda x: 1 - np.cos(x)

N_list = int(1E+5)

N_search = int(1E+7)
search_data = [(-1) ** i for i in range(N_search)]
search_term = +1
correct_search = N_search // 2

# ==================================================================================================================== #
# helper functions and constants

def timed(f):
    def inner(*args, **kwargs):
        tic = time.perf_counter()
        result = f(*args, **kwargs)
        toc = time.perf_counter()
        return result, toc - tic, f.__name__
    return inner


table_header    = "name                     | delta to correct | runtime"
table_separator = "-------------------------+------------------+-------------"
table_fields    = "{name:25}|{delta:18.4E}|{runtime:10.3f} ms"

def print_result_line(result, category):
    delta = 0
    if category == "integral":
        delta = result[0] - correct_integral(upper_bound_integral)
    elif category == "sum":
        delta = result[0] - correct_sum(N_sum)
    elif category == "search":
        delta = result[0] - correct_search
    else :
        delta = float("nan")

    print(table_fields.format(name=result[2],
                              delta=delta,
                              runtime=result[1] * 1000))

# ==================================================================================================================== #
# summation
# all of these functions compute the sum of an array of integers

@timed
def sum_naive():
    result = 0
    for num in data_sum:
        result += num
    return result

@timed
def sum_builtin():
    return sum(i for i in data_sum)

@timed
def sum_numpy():
    return np.array(data_sum).sum()

@timed
def sum_numpy_no_allocate(data):
    return data.sum()

@timed
def sum_expression():
    return correct_sum(N_sum)

# -------------------------------------------------------------------------------------------------------------------- #
# integration
# all of these compute the integral from 0 to pi over sin(t) dt

@timed
def integral_naive(dt):
    result = 0
    x = 0
    while x < upper_bound_integral:
        result += integrand(x) * dt
        x += dt
    return result

@timed
def integral_numpy(dt):
    return integrand(np.arange(0, upper_bound_integral, dt)).sum() * dt

@timed
def integral_scipy_quad():
    return scInt.quad(integrand, 0, upper_bound_integral)[0]

@timed
def integral_scipy_gaussian():
    return scInt.fixed_quad(integrand, 0, upper_bound_integral)[0]

@timed
def integral_expression():
    return correct_integral(upper_bound_integral)

# ==================================================================================================================== #
# building a list
# all of these functions create a list of integers with values 0..N_list

@timed
def list_comprehension():
    return [i for i in range(N_list)]

@timed
def list_append():
    result = []
    for i in range(N_list) :
        result.append(i)
    return result

@timed
def list_numpy_arange():
    return np.arange(N_list)

@timed
def list_numpy_append():
    result = np.array([])
    for i in range(N_list):
        result = np.append(result, i)
    return result

# ==================================================================================================================== #
# count test
# all of these count how often a search term appears in a list of integers

@timed
def count_naive(data, search):
    result = 0
    for element in data:
        if element == search : result += 1
    return result

@timed
def count_builtin(data, search):
    return data.count(search)

@timed
def count_numpy(data, search):
    return np.count_nonzero(np.array(data) == search)

# ==================================================================================================================== #

if __name__ == '__main__':
    print(table_header)
    print(table_separator)

    print_result_line(sum_naive(), "sum")
    print_result_line(sum_builtin(), "sum")
    print_result_line(sum_numpy(), "sum")
    data = np.arange(N_sum)
    print_result_line(sum_numpy_no_allocate(data), "sum")
    print_result_line(sum_expression(), "sum")

    print(table_separator)

    print_result_line(integral_naive(dt), "integral")
    print_result_line(integral_numpy(dt), "integral")
    print_result_line(integral_scipy_quad(), "integral")
    print_result_line(integral_scipy_gaussian(), "integral")
    print_result_line(integral_expression(), "integral")

    print(table_separator)

    print_result_line(list_comprehension(), "list")
    print_result_line(list_append(), "list")
    print_result_line(list_numpy_arange(), "list")
    print_result_line(list_numpy_append(), "list")

    print(table_separator)

    search_data_np = np.array(search_data)
    print_result_line(count_naive(search_data, search_term), "search")
    print_result_line(count_builtin(search_data, search_term), "search")
    print_result_line(count_numpy(search_data, search_term), "search")
    print_result_line(count_numpy(search_data_np, search_term), "search")