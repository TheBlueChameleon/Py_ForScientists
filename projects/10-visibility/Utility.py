print("ABOUT TO INITIALIZE Utility.py")

import Constants as Consts
from Constants import Constants


class Utility:
    @staticmethod
    def show_constants():
        print("ALL KNOWN CONSTANTS IN CLASS Constants AS SEEN FROM Utility.py:")
        for name, value in Constants.__dict__.items():
            if name.startswith("__"): continue
            print(f"  {name} = {value}")

        print("READING Consts.MODULE_LEVEL_CONSTANT IN Utility.py:", Consts.MODULE_LEVEL_CONSTANT)
        print("READING Consts.MUTALBE_MODULE_LEVEL_CONSTANT IN Utility.py:", Consts.MUTALBE_MODULE_LEVEL_CONSTANT)


print("DONE INITIALIZING Utility.py")
