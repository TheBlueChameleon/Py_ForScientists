import multiprocessing as mp
import sys
import time


def subprocess():
    time.sleep(5)
    print(f"{mp.current_process().name} done")


def main():
    processes = [mp.Process(target=subprocess) for _ in range(4)]

    for p in processes:
        p.start()

    print("done")
    sys.exit(0)

    # "Forgetting" to join the created subprocesses here -- this causes trouble:
    # The subprocesses remain in the "zombie" state until the OS cleans them up, which takes some time
    # That means, there's a (usually temporary) resource leak. Not too bad on modern OS'es, but bad style.
    # In particular, the processes static memory may remain in use in some cases.
    # You can watch your system activity (e.g. in task manager) to see instances of the Python interpreter remain listed
    # albeit the code execution has long finished.


if __name__ == "__main__":
    main()