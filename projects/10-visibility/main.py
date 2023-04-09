# The second import of constants is to show how the different methods have slightly different behaviour.
# See Constants.py for more explanations.
import Constants as Consts
from Constants import Constants
from Utility import Utility


def main():
    print("READ ACCESS TO A MEMBER OF CLASS Constants:", Constants.PROJECT_NAME_VERSIONED)

    Consts.MODULE_LEVEL_CONSTANT += " altered by main"
    print("WRITE ACCESS TO Consts.MODULE_LEVEL_CONSTANT IN main.py:", Consts.MODULE_LEVEL_CONSTANT)

    Constants.WRITE_ACCESS = "changed"
    print("WRITE ACCESS TO Constants.WRITE_ACCESS IN main.py sees:", Constants.WRITE_ACCESS)

    Consts.MUTALBE_MODULE_LEVEL_CONSTANT.append("mutable variable access successful")

    Utility.show_constants()


if __name__ == '__main__':
    main()
