import sys

import TextTools

def main():
    TextTools.print_head("Well Documented Code Project")
    TextTools.log("this log message goes to the disk")
    TextTools.log("this log message goes to the screen", TextTools.LogLevel.Warning, sys.stdout)
    TextTools.print_decobar(80, TextTools.logfile)
    print("Regular output")


if __name__ == '__main__':
    main()

