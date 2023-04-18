import multiprocessing as mp
import time


def producer(ID, queue, done, lock):
    lock.acquire()
    print("producer", ID, "begins production")
    lock.release()

    while not done.value:
        lock.acquire()
        print("producer", ID, "produces goods")
        lock.release()

        time.sleep(.1)
        queue.put(f"stuff from producer #{ID}")


def consumer(ID, queue, done, lock):
    lock.acquire()
    print("consumer", ID, "begins consumption")
    lock.release()

    while not done.value:
        time.sleep(.2)
        msg = f"consumer {ID} "
        if queue.empty():
            msg += "takes a day off."
        else:
            msg += "consumes " + queue.get()
        lock.acquire()
        print(msg)
        lock.release()


def main():
    lock = mp.Lock()
    queue = mp.Queue()
    done = mp.Value('b', False)
    nProducers = 5
    nConsumers = 10
    worktime = 5

    processes = []
    for i in range(nProducers):
        processes.append(mp.Process(target=producer, args=(i, queue, done, lock)))

    for i in range(nConsumers):
        processes.append(mp.Process(target=consumer, args=(i, queue, done, lock)))

    for p in processes:
        p.start()

    time.sleep(worktime)
    done.value = True

    for p in processes:
        p.join()

    print("unconsumed goods:", queue.qsize())


if __name__ == '__main__':
    main()
