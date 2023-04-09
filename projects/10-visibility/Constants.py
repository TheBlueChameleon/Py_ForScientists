# Note:
# Code on module level runs only when the module is loaded for the first time.
# In this project, we have the modules main.py and Utility.py, both of which import Constants.py.
# Python keeps track which modules are already loaded. So after "properly" loading Constants in main, Python does not
# re-initialize the module when it arrives at the import Constants in Utility.py.
# This does not mean that we can omit the import statement in Utility.py -- it is still needed to make the symbols
# visible within Utility.py.

print("ABOUT TO INITIALIZE Constants.py")


class Constants:
    VERSION_MAJOR = 1
    VERSION_MINOR = 0
    PROJECT_NAME = "Parametrized Template"

    # this variable will be overwritten in several points. See notes near MODULE_LEVEL_CONSTANT below.
    WRITE_ACCESS = "unchanged"

    # unfortunately, we cannot use the above symbols to define this constant, because the name Constants is not
    # registered yet (we're only about to define the class and cannot refer to an incomplete object.
    # but we can provide a dummy slot ...
    PROJECT_NAME_VERSIONED = None


# ... and fill it out once we've fully defined the class.
Constants.PROJECT_NAME_VERSIONED = f"{Constants.PROJECT_NAME} v{Constants.VERSION_MAJOR}.{Constants.VERSION_MINOR}"

# You could also simply put your constants on module level directly:
MODULE_LEVEL_CONSTANT = "module level constant"
# in main.py you'll find the line
#  import Constants as Consts
# where the as clause is only needed because the symbol Constants is already in use.
# however, this approach only works for read-only attributes.

MUTALBE_MODULE_LEVEL_CONSTANT = []

print("DONE INITIALIZING Constants.py")
