# The Travelling Salesman Problem (TSP) is a famous standard problem im computer science.
# The (basic) problem statement is the following:
#   Given a list of points (cities) to visit, what is the shortest path through all of them?
# The only known algorithm guaranteed to always find the shortest route is a brute force analysis of all possible
# routes, which has atrocious time complexity of O(N!).
# (There are N possible choices for the start city, from which one can visit (N-1) cities as second stop, from which
# one can visit (N-2) cities as third stop, etc.).
# A number of algorithms have been proposed that do not necessarily produce the best, but a "reasonably good" solution,
# i.e. one that is in the top 10% of all possible paths, while having a way better runtime.
# The code below shows both, a brute force implementation of the TSP as well as an approximation based on the following
# idea:
#   The next step in the path is always the city closest to the current one.
# This works extraordinarily well for small numbers of cities (where the brute force approach would be viable, too), but
# may be forced to make suboptimal choices toward the end of the path.
# Runtime is O(N²): For each current city, we have to compute the lengths to O(N) other cities in order to find the
# shortest next path segment. So the approximation brings the problem from "impossible for long lists of points" to
# "viable for virtually any problem size".
# Usually, the paths found that way are pretty decent, too. The biggest flaw is that the starting point is often not
# optimal (which, in real world problems, might not be a degree of freedom to freely chose anyway).
# Note: an improved form of this algorithm exists (not implemented here), where the path generated in the way described
# above is checked for crossing lines. If any are detected, their targets are exchanged. This path is always shorter,
# which is a consequence of the triangle inequality.
# Here, we are not so much interested in the solutions as in the implementation using itertools.

import itertools
import math
import random
import sys
import time
import typing

import matplotlib.pyplot as plt

# well... not infinity, but the biggest number that can be stored as a float.
# We'll use that for comparing lengths in the TSP.
infinity = sys.float_info.max


def get_points(n_tuples: int, n_dims: int) -> list[tuple]:
    """
    Produces a list of points in N-dimensional space

    :param n_tuples: the number of points to generate
    :param n_dims: the number of spatial dimensions per point
    :return: a list of coordinates
    """

    # Note: It would be way more convenient to simply
    #  return np.random.random(size=(n_tuples, n_dims))
    # The below code illustrates how to construct groups from a sequence of data items
    # As a consequence, the rest of this example uses Python-native data types, too.

    data = (random.random() for _ in range(n_tuples * n_dims))
    # data is a generator object, so [data] * n_dims contains only the instruction to evaluate random.random() n_dims times.
    accessor = [data] * n_dims
    # zip continues until any object passed to it is exhausted. Since we pass n_dims times the same object data, we simply
    # read all numbers in the generator and pack them into tuples.
    return [pack for pack in zip(*accessor)]


def distance_between(point_a: tuple[float], point_b: tuple[float]) -> float:
    """
    Computes the euclidian distance between two points in n-dimensional space.

    :param point_a: coordinates of the first point as an iterable of floats
    :param point_b: coordinates of the second point as an iterable of floats
    :return: the euclidean distance as a float
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point_a, point_b)))


def track_length(points: typing.Iterable[tuple]) -> float:
    """
    Computes the euclidean length of a path, given by a sequence of points.

    :param points: The path to compute, given as an iterable of n-dimensional tuples
    :return: The lenght of the path, as a float.
    """

    # itertools.pairwise("ABC") gives ('A', 'B'), ('B', 'C')
    neighbours = itertools.pairwise(points)
    return sum(itertools.starmap(distance_between, neighbours))


def solve_tsp_exhaustive(points: list[tuple]) -> typing.Tuple[list[tuple], float]:
    """
    Computes the optimal path through a collection of points along with the path length

    :param points: an iterable of n-dimensional coordinates for which to find the optimal path
    :return: a tuple consisting of the optimal path (i.e. a permutation of points) and the associated length
    """
    paths: typing.Iterable = itertools.permutations(points)
    solution: tuple = None
    # we compare each candidate path in paths against the best path found so far. Since at this point, we haven't found
    # any solution, we give it the worst possible length, which is "infinity" (or rather, the biggest number a float can
    # handle).
    length: float = infinity

    for candidate in paths:
        candidate_length = track_length(candidate)
        if candidate_length < length:
            length = candidate_length
            solution = candidate

    return solution, length


def solve_tsp_approximative(points: list[tuple], start: int = 0) -> typing.Tuple[list[tuple], float]:
    """
    Computes a reasonably short path through a collection of points along with the path length

    :param start: The index of the point in which the generated path should start.
    :param points: an iterable of n-dimensional coordinates for which to find the optimal path
    :return: a tuple consisting of the optimal path (i.e. a permutation of points) and the associated length
    """

    last_point = points[start]
    unvisited_points = [True for _ in points]
    unvisited_points[start] = False

    solution = [last_point]
    total_length = 0

    while any(unvisited_points):
        best_id = None
        best_length = infinity

        remaining_points = itertools.compress(points, unvisited_points)
        for point in remaining_points:
            length = distance_between(last_point, point)
            if length < best_length:
                best_id = points.index(point)
                # cannot use enumerate(remaining_points): indices do not match those of points...
                best_length = length

        unvisited_points[best_id] = False
        last_point = points[best_id]
        solution.append(last_point)
        total_length += best_length

    return solution, total_length


def main():
    n_cities = 9
    n_dims = 2
    points = get_points(n_cities, n_dims)

    print("RANDOMLY GENERATED POINTS")
    for point in points:
        print("  ", point)
    print()
    print("TRACK LENGTH WHEN TRAVERSING IN THIS ORDER:")
    print("  ", track_length(points))

    print("BEGINNING TO FIND BEST ROUTE ... ", end="")
    tic = time.perf_counter()
    best_solution, best_length = solve_tsp_exhaustive(points)
    toc = time.perf_counter()
    time_best_solution = toc - tic
    print("DONE!")
    for point in best_solution:
        print("  ", point)
    print(f"   track length = {best_length}, took {time_best_solution:5.3}s")

    print("BEGINNING TO FIND OKAY ROUTE ... ", end="")
    tic = time.perf_counter()
    approximate_solution, approximate_length = solve_tsp_approximative(points)
    toc = time.perf_counter()
    time_approximate_solution = toc - tic
    print("DONE!")
    for point in approximate_solution:
        print("  ", point)
    print(f"   track length = {approximate_length}, took {time_approximate_solution:5.3}s")

    plt.title("Travelling Salesman Problem")
    plt.plot(*zip(*points), "o", label="Given Coordinates")
    plt.plot(*zip(*best_solution), label=f"Best Solution (l={best_length:5.3f})")
    plt.plot(*zip(*approximate_solution), "--", label=f"Approximate Solution (l={approximate_length:5.3f})")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
