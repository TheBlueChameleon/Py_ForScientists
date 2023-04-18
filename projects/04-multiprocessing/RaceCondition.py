import multiprocessing as mp
import time


def worker(name):
    print("This is worker ", name, " (", mp.current_process().name, ") ", "beginning to do my job", sep="", flush=True)
    time.sleep(1)
    print("Worker", name, "has finished doing their job")


def worker_with_lock(name, lock):
    lock.acquire()
    print("This is worker ", name, " (", mp.current_process().name, ") ", "beginning to do my job", sep="", flush=True)
    lock.release()

    time.sleep(1)

    lock.acquire()
    print("Worker", name, "has finished doing their job")
    lock.release()


def main():
    names = ["Caspar", "Charlotte", "Alex", "Jasmin"]
    lock = mp.Lock()

    print("NO LOCKS")
    tic = time.time()
    processes = [mp.Process(target=worker, args=(name,)) for name in names]
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()
    toc = time.time()

    print()
    print("All workers have finished their jobs.")
    print("Time elapsed:", toc - tic, "seconds")
    print()

    print("LOCK ACTIVE")
    tic = time.time()
    processes = [mp.Process(target=worker_with_lock, args=(name, lock)) for name in names]
    for proc in processes: proc.start()
    for proc in processes: proc.join()
    toc = time.time()

    print()
    print("All workers have finished their jobs.")
    print("Time elapsed:", toc - tic, "seconds")
    print()

    print("POOL VERSION")
    pool = mp.Pool(mp.cpu_count())
    for name in names:
        pool.apply_async(worker, (name,))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
