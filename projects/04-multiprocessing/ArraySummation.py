import multiprocessing as mp
import time


def sum_slice(data, start, stop, total: mp.Value):
    partial_sum = sum(data[start:stop])
    with total.get_lock():
        total.value += partial_sum


def main():
    N = 16_000_000
    data = mp.Array("i", list(range(N)), lock=False)
    total = mp.Value("q", 0)

    tic = time.perf_counter()
    classic = sum(data)
    toc = time.perf_counter()

    print("Classic : got", classic, f"in {(toc - tic) * 1000:4.2f} ms")

    n_workers = mp.cpu_count() // 2
    slice_size = N // n_workers
    processes = [mp.Process(target=sum_slice,
                            args=(data, i * slice_size, (i + 1) * slice_size, total)
                            ) for i in range(n_workers)]

    tic = time.perf_counter()
    for p in processes: p.start()
    for p in processes: p.join()
    toc = time.perf_counter()

    print("Parallel: got", total.value, f"in {(toc - tic) * 1000:4.2f} ms")


if __name__ == '__main__':
    main()
