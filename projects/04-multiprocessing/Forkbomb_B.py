import multiprocessing as mp

# keep these numbers low if you value your computer.
n_processes_per_level = 2
max_levels = 5


# in total, there will be
#   sum_{i=0}^{max_levels} n_processes_per_level^i
# processes, which is in O(a metric fuckton)

def forkbomb(process_count):
    with process_count.get_lock():
        process_count.value += 1

    name = mp.current_process().name
    if name == "MainProcess":
        level = 0
    else:
        # each subprocess has a name like "Process-1:2:1:2"
        # so by counting the number of colons, we get how many layers into the forkbomb we've gotten
        level = name[8:].count(':') + 1

    print(f"#{process_count.value}: {name} at level {level}\n", end="")

    if level < max_levels:
        processes = [mp.Process(target=forkbomb, args=(process_count,)) for _ in range(n_processes_per_level)]

        for p in processes:
            p.start()

        for p in processes:
            p.join()


def main():
    process_count = mp.Value('i', 0)
    forkbomb(process_count)


if __name__ == "__main__":
    main()
