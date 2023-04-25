import cmath
import typing

Number = typing.Union[int, float, complex]
Vector = typing.Collection[Number]


def dot_product(a: Vector, b: Vector) -> Number:
    if len(a) != len(b):
        # if using a linter, it is guaranteed that a and b are compatible with len, because they are of type Collection
        # input might still be nonsensical, but at least we can make sure we get a meaningful error message.
        raise AttributeError("Vectors do not have same length!")

    return sum(x * y for x, y, in zip(a, b))


def vector_length(v: Vector) -> Number:
    return cmath.sqrt(dot_product(v, v))


def return_untyped_data():
    return ['1', '2', '3']


def main() -> None:
    print(vector_length.__annotations__)

    foo = [1, 2, 3]
    print(vector_length(foo))

    # this will give a runtime error, but the linters should already warn you that this is the case
    try:
        bar: list['str'] = ['1', '2', '3']
        print(vector_length(bar))
    except TypeError:
        print("--- PREVENTABLE ERROR ---")

    # depending on which linter you use, you might even get a warning on this call
    try:
        print(vector_length(return_untyped_data()))
    except TypeError:
        print("--- PREVENTABLE ERROR ---")


if __name__ == "__main__":
    main()
