class Foo():
    def __init__(self):
        self.value = "the Foo"

    def __enter__(self):
        print("Entering context of Foo")
        return self

    def __exit__(self, err_type, err_value, traceback):
        print("Leaving context of Foo")


def main():
    with Foo() as foo:
        print(foo.value)


if __name__ == '__main__':
    main()
