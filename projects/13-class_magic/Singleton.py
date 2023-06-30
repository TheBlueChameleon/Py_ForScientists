class Singleton:
    _instance = None
    init_attempts = 0

    def __init__(self):
        self.init_attempts += 1

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Derived(Singleton):
    def __init__(self):
        # This method will never be run if another Singleton has been instantiated before.
        # Reason:
        #   Derived() invokes Derived.__call__().
        #   This in turn first obtains a new object by means of __new__(Derived, *args, **kwargs).
        #   Only if the obtained instance is an instance of Derived, instance.__init__(*args, **kwargs) is called.
        #   Since there is already another Singleton instantiated, this condition is not satisfied.

        super().__init__()
        self.attribute = "this is derived"


def main():
    instance_1 = Singleton()
    instance_2 = Singleton()

    print("instance_1 and instance_2 are ", end="")
    if id(instance_1) == id(instance_2):
        print("the ame")
    else:
        print("different")
    print()

    print("Problem: You cannot (meaningfully) derive from the Singleton class")
    derived_instance = Derived()
    print("derived_instance and instance_2 are the same:", derived_instance is instance_2)
    print()

    try:
        print(derived_instance.attribute)
    except AttributeError:
        print("Initialization of Derived has been prevented")

    print("Number of initializations:", derived_instance.init_attempts)


if __name__ == '__main__':
    main()
