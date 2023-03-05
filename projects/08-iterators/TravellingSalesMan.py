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
    # Note: It would be way more convenient to simply
    #  return np.random.random(size=(n_tuples, n_dims))
    # The below code illustrates how to construct groups from a sequence of data items
    # As a consequence, the rest of this example uses Python-native data types, too.

    data = (random.random() for _ in range(n_tuples * n_dims))
    accessor = [data] * n_dims
    return [tuple(pack) for pack in zip(*accessor)]


def distance_between(point_a: tuple[float], point_b: tuple[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point_a, point_b)))


def track_length(points: typing.Iterable[tuple]) -> float:
    neighbours = itertools.pairwise(points)
    return sum(itertools.starmap(distance_between, neighbours))


def solve_tsp_exhaustive(points: list[tuple]) -> typing.Tuple[list[tuple], float]:
    paths: typing.Iterable = itertools.permutations(points)
    solution: tuple = None
    length: float = infinity

    for candidate in paths:
        candidate_length = track_length(candidate)
        if candidate_length < length:
            length = candidate_length
            solution = candidate

    return solution, length


def solve_tsp_approximative(points: list[tuple], start: int = 0) -> typing.Tuple[list[tuple], float]:
    last_point = points[start]
    unvisited_points = [1 for _ in points]
    unvisited_points[start] = 0

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

        unvisited_points[best_id] = 0
        last_point = points[best_id]
        solution.append(last_point)
        total_length += best_length

    return solution, total_length


def main():
    n_foo = 9
    n_dims = 2
    points = get_points(n_foo, n_dims)

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
