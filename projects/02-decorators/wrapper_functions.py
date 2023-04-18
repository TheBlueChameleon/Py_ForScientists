def announce(f):
    def inner(*args, **kwargs):
        print("calling", f.__name__, "with arguments", args, kwargs)
        result = f(*args, **kwargs)
        print("returning from", f.__name__, "with result", result)
        print()
        return result

    return inner


def minimal():
    print("inside minimal")


def return_something():
    print("inside return_something")
    return "something"


def take_arguments(a, b):
    print("inside take_arguments")
    return a + b


@announce
def directly_modified():
    print("inside directly_modified")


def main():
    minimal_modified = announce(minimal)
    return_something_modified = announce(return_something)
    take_arguments_modified = announce(take_arguments)

    minimal_modified()
    return_something_modified()
    take_arguments_modified(1, 2)
    directly_modified()


if __name__ == '__main__':
    main()
