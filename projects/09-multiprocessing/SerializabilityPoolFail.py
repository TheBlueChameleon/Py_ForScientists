import multiprocessing as mp


# ==================================================================================================================== #
# function worker is a regular, non-nested function -- everything works fine.

def worker():
    print(mp.current_process().name)


def flattened():
    n_threads = mp.cpu_count()
    pool = mp.Pool(n_threads)
    for _ in range(n_threads):
        pool.apply_async(worker)
    pool.close()
    pool.join()
    print()


# ==================================================================================================================== #
# If you put the worker inside the function calling it, things go south.
# You'll see the error message
#   AttributeError: Can't pickle local object 'nested.<locals>.nested_worker'
# if you try to run this, because Pool tries to communicate the tasks it's been given to yet another process

def nested():
    def nested_worker():
        print(mp.current_process().name)

    pool = mp.Pool(4)
    pool.apply(nested_worker)
    print()


# ==================================================================================================================== #
# This limitation does not hold in general when doing multiprocessing. Starting the subprocesses by hand, we can use
# a nested function as target just fine.

def nested_no_pool():
    def nested_worker():
        print(mp.current_process().name)

    processes = [mp.Process(target=nested_worker) for _ in range(mp.cpu_count())]

    for p in processes: p.start()
    for p in processes: p.join()

# ==================================================================================================================== #

def main():
    # show that pool works in principle
    flattened()

    # the code behind this function fails; see comments above for why that is.
    # nested()

    # show that nested functions themselves are NOT the problem
    nested_no_pool()


if __name__ == "__main__":
    main()
