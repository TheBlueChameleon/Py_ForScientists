from Globals import Globals
from Logger import Logger


# for example, run with
#   python3 main.py sample_1.inp sample_2.inp --deb --settings settings.ini

def main():
    print("#" * 80)
    Globals.show_all()

    print("#" * 80)
    print("Unconditional output to stdout")
    Logger.log("Unconditional output to log file")
    Logger.debuglog("Conditional output to log file (only if --debug is set)")

    print("#" * 80)
    # note that I overloaded the __getattr__ method in GlobalsClass in order to make these lines work:
    print("Regular global object:", Globals.PROJECT_NAME)
    print("CLI parameter:", Globals.debug)
    print("Settings file element:", Globals.FILES["output_filename"])

    print("All keys in [SIMULATION]:")
    for foo in Globals.SIMULATION:
        print(f"- {foo}")


if __name__ == '__main__':
    main()
