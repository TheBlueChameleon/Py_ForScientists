import multiprocessing as mp
import random

n_cpus = mp.cpu_count() // 2
needles_to_hide = 5
haystack_size = 1_000_000

needles_found = 0

# using variables for constants prevents typos
NEEDLE = "needle"
STRAW = "straw"


# ==================================================================================================================== #

def prepare_haystack(n_needles):
    print("preparing haystack ... ", end="")

    haystack = [STRAW] * haystack_size

    for _ in range(n_needles):
        good_spot = False  # only put needles where there is not already another needle.
        while not good_spot:
            i = random.randint(0, haystack_size)
            if haystack[i] == STRAW:
                good_spot = True
                haystack[i] = NEEDLE

    print("done")
    return haystack


# ==================================================================================================================== #

def worker_globals(element):
    global needles_found
    if element == NEEDLE:
        needles_found += 1


def find_needles_globals(haystack):
    global needles_found
    pool = mp.Pool(n_cpus)
    pool.map(worker_globals, haystack)


# ==================================================================================================================== #

def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


def worker_shared_variable(elements, counter):
    for element in elements:
        if element == NEEDLE:
            with counter.get_lock():
                counter.value += 1


def find_needles_shared_variable(haystack, counter):
    N = len(haystack)
    chunksize, remainder = divmod(N, n_cpus)
    if remainder > 0:
        chunksize += 1

    chunks = split(haystack, chunksize)
    processes = [mp.Process(target=worker_shared_variable, args=(chunk, counter)) for chunk in chunks]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


# ==================================================================================================================== #

def main():
    haystack = prepare_haystack(needles_to_hide)

    # just to prove that the haystack holds any needles at all
    print("Single threaded search finds", haystack.count('needle'), "needles")

    # this is bound to fail: each process has its own variable needles_found, and they do not communicate.
    find_needles_globals(haystack)
    # consequently, this will claim to have found zero needles in the haystack.
    print("Multiprocess search via global variable finds", needles_found, "needles")

    # using an inter-process variable, we can split the work and still get the results
    shared_counter = mp.Value('i', 0)
    find_needles_shared_variable(haystack, shared_counter)
    print("Multiprocess search via shared variable finds", shared_counter.value, "needles")


if __name__ == "__main__":
    main()
