import atexit
import sys
from datetime import datetime
from enum import StrEnum

# happens as soon as the file is imported
logfile = open("logfile.txt", "w")


class LogLevel(StrEnum):
    """Enumerates the constants used as log levels"""

    Info = "Info"
    Warning = "Warning"
    Error = "Error"


def log(text: str, level: LogLevel = LogLevel.Info, file=logfile) -> None:
    """
    Writes a log message with fixed format.
    By default, output happens in the logfile, but can be directed to any file stream

    :param text: The message to be logged
    :param level: A classification of the log message so that logs can be filtered for relevant details
    :param file: The file stream in which to write the message
    """
    print(f"[{datetime.now()}] {level:8}:", text, file=file)
    pass


def test_module() -> None:
    """
    This is where you would write code that showcases the features of the (sub)module or tests its functionality.
    """
    print("some tests here")


def shutdown():
    """
    Closes the log file and thus ensures the buffer is actually written to disk.
    Automatically invoked.
    """
    print("shutting down logger", file=sys.stderr)
    logfile.close()


# this makes it so that shutdown is automatically called when the program ends.
atexit.register(shutdown)

if __name__ == "__main__":
    test_module()
