"""
Logger Tools

Facilitates logging events to disk
"""

import atexit


def log(text):
    print(text, file=logfile)


def test_module():
    print("some tests here")


def shutdown():
    print("shutting down logger")
    logfile.close()


logfile = open("logfile.txt", "w")  # happens no matter what
atexit.register(shutdown)

if __name__ == "__main__":  # happens only when this
    test_module()  # is the main module.
