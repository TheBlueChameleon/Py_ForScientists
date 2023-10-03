# To run this file, simply navigate to the parent directory (20-networking) and, on the console, invoke
#   python3 -m EchoSimple Server
# or
#   python3 -m EchoSimple Client
# This first executes __init__, and then runs __main__.
# The option -m means "run as module", which triggers exactly this behaviour (run init, then main).

import sys
from EchoSimple import Server, Client, Constants

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        print("EchoSimple. Use:")
        print("  python3 -m EchoSimple <mode>")
        print("where <mode> is either 'Server' or 'Client'.")
    else:
        mode = args[1].upper()
        if mode == "SERVER":
            Server.server()
        elif mode == "CLIENT":
            Clent.client()
        else:
            print(f"Unknown Mode: '{mode}'")
