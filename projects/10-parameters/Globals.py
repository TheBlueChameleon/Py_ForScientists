import argparse
import configparser
import sys


class GlobalsClass:
    def __init__(self):
        self.VERSION_MAJOR = 1
        self.VERSION_MINOR = 0
        self.PROJECT_NAME = "Parametrized Template"

        # initializing all members here improves IDE support
        self.PROJECT_NAME_VERSIONED = None
        self.CLI_ARGUMENTS = None
        self.CLI_ARGUMENT_NAMES = None
        self.SETTINGS_FILE_CONTENT = None
        self.LOG_FILE = None

        self.init_dependent_globals()

    def init_dependent_globals(self):
        self.PROJECT_NAME_VERSIONED = f"{self.PROJECT_NAME} v{self.VERSION_MAJOR}.{self.VERSION_MINOR}"

        self.parse_command_line()
        self.parse_settings_file()

    def parse_command_line(self):
        parser = argparse.ArgumentParser(description="runs a simulation")

        parser.add_argument("inputFiles", nargs="+")
        parser.add_argument("--logfile", help="redirects help to a file")
        parser.add_argument("--settings", default="settings.ini")
        parser.add_argument("--debug", action='store_true')

        # For example, invoke with
        #   python3 main.py sample_1.inp sample_2.inp --debug --settings settings.ini
        # Order of optional arguments is not important

        self.CLI_ARGUMENTS = parser.parse_args()

        if self.CLI_ARGUMENTS.logfile is None:
            # if no logfile was provided: write on screen (standard output, aka stdout)
            self.LOG_FILE = sys.stdout
        else:
            # try to open logfile and use it as output for all logs
            logfilename = self.CLI_ARGUMENTS.logfile
            try:
                handle = open(logfilename, "w")
            except IOError:
                # if this fails, default to output on screen
                # also write an error message to the standard error device (stderr; usually also the screen)
                print(f"COULD NOT OPEN LOGFILE '{logfilename}'. OUTPUT REDIRECTED TO STDOUT.", file=sys.stderr)
                handle = sys.stdout
            self.LOG_FILE = handle

    def parse_settings_file(self):
        settings_file = self.CLI_ARGUMENTS.settings
        config = configparser.ConfigParser(interpolation=None)
        config.read(settings_file)

        self.SETTINGS_FILE_CONTENT = config

    def show_all(self):
        special_members = ["CLI_ARGUMENTS", "SETTINGS_FILE_CONTENT"]

        print("Constants")
        for name, value in vars(self).items():
            if name.startswith("__") or callable(value) or name in special_members:
                continue
            print(f"  {name} = {value}")

        print("Command Line Parameters")
        for name, value in vars(self.CLI_ARGUMENTS).items():
            print(f"  {name} = {value}")

        print("Settings File Content")
        for section in self.SETTINGS_FILE_CONTENT:
            print(f"  section {section}:")
            for key, value in self.SETTINGS_FILE_CONTENT[section].items():
                print(f"    {key} = {value}")

    def __getattr__(self, item):
        # resolves read access like Globals.item
        # extends lookup to CLI params and settings file content

        if item in vars(self):
            return vars(self)[item]
        elif item in self.CLI_ARGUMENTS:
            return vars(self.CLI_ARGUMENTS)[item]
        elif item in self.SETTINGS_FILE_CONTENT:
            return self.SETTINGS_FILE_CONTENT[item]
        else:
            raise AttributeError(f"Attribute '{item}' does not exist")


Globals = GlobalsClass()
