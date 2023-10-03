import EchoSimple
import MultiConnection

import time
import multiprocessing as mp


def start_as_subprocesses_with_delay(routines_or_delays):
    """
    Runs an arbitrary list of functions as new processes and adds pauses of arbitrary length between starting some
    of the processes

    :param routines_or_delays: A list containing callables and floats.
        The callables will be started as new processes.
        floats represent the waiting time in seconds before starting the next process.
    """
    procs = []
    for rod in routines_or_delays:
        if callable(rod):
            procs.append(mp.Process(target=rod))
            procs[-1].start()
        else:
            time.sleep(rod)

    for proc in procs:
        proc.join()


def echo_simple():
    """
    First starts a server as a new process. Waits for 0.1 seconds to ensure the server is ready to accept
    connections before starting the client as a new process, too.
    """
    start_as_subprocesses_with_delay([EchoSimple.server, 0.1, EchoSimple.client])


def mcp_server(max_runtime_seconds):
    def inner():
        s = MultiConnection.Server(max_runtime_seconds)
        s.run()

    return inner


def mcp_client(client_id):
    def inner():
        c = MultiConnection.Client(client_id)
        c.run()

    return inner


def multiple_clients_protocol():
    clients = (mcp_client(i) for i in range(2))
    start_as_subprocesses_with_delay([mcp_server(1), 0.1, *clients])


def main():
    echo_simple()
    multiple_clients_protocol()


if __name__ == '__main__':
    main()
