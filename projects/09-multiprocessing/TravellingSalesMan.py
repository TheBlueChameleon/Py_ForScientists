import itertools
import multiprocessing as mp
import time

import matplotlib.pyplot as plt
import numpy as np

n_cpus = mp.cpu_count()


def get_points(n_tuples, n_dims):
    return np.random.random(size=(n_tuples, n_dims))


def track_length(points):
    next_neighbours = np.roll(points, 1, axis=0)
    differences = (points - next_neighbours)[1:, :]
    return np.sum(np.sqrt(np.sum(differences ** 2, axis=1)))


def solve_tsp_exhaustive(points, n_workers=n_cpus):
    all_paths = list(itertools.permutations(points))

    pool = mp.Pool(n_workers)
    lengths = pool.map(track_length, all_paths)
    pool.close()
    pool.join()

    best_idx, best_length = min(enumerate(lengths), key=lambda tuple_of_idx_and_length: tuple_of_idx_and_length[1])
    return all_paths[best_idx], best_length


def run_and_plot():
    n_cities = 9
    n_dims = 2
    points = get_points(n_cities, n_dims)

    best_path, best_length = solve_tsp_exhaustive(points)

    plottable_path = np.stack(best_path)

    plt.title("Travelling Salesman Problem")
    plt.plot(points[:, 0], points[:, 1], "o", label="Given Coordinates")
    plt.plot(plottable_path[:, 0], plottable_path[:, 1])
    plt.show()


def measure_overhead():
    n_cities = 8
    n_dims = 2
    points = get_points(n_cities, n_dims)

    n_max_processes = int(1.5 * n_cpus)
    times = np.zeros(n_max_processes)

    n_processes = np.arange(1, n_max_processes + 1)
    for n in n_processes:
        print("Measuring performance with", n, "processes ... ", end="")
        tic = time.perf_counter()
        solve_tsp_exhaustive(points, n)
        toc = time.perf_counter()
        print("done.")
        times[n - 1] = (toc - tic) * 1000

    print("N_processes | Runtime in ms")
    print("------------+--------------")
    for n, t in zip(n_processes, times):
        print(f"{n:^12}| {t:12.3f}")

    plt.title("Timing Results")
    plt.plot(n_processes, times, label="measured runtime")
    plt.plot(n_processes, times[0] / n_processes, "o", label="1/n behaviour")
    plt.xlabel("Number of processes")
    plt.ylabel("Runtime in ms")
    plt.legend()
    plt.show()


def main():
    # run_and_plot()
    measure_overhead()


if __name__ == '__main__':
    main()
