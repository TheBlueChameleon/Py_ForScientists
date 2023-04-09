from Globals import Globals

class Logger:
    @staticmethod
    def log(*args):
        print(*args, file=Globals.LOG_FILE)

    @staticmethod
    def debuglog(*args):
        if (Globals.debug):
            Logger.log(*args)