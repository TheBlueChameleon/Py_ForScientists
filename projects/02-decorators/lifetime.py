import sys


# ===================================================================================================================== #

def is_and_equals():
    A = [1, 2]
    B = A
    C = [1, 2]

    print("id(A) = ", id(A))
    print("id(B) = ", id(B))
    print("id(C) = ", id(C))
    print()

    print("A == B:", A == B)
    print("A == C:", A == C)
    print("B == C:", B == C)
    print()

    print("A is B:", A is B)
    print("A is C:", A is C)
    print("B is C:", B is C)


# ===================================================================================================================== #

def return_immutable():
    x = "some value"
    return x


def return_mutable():
    x = ["some value"]
    return x


def return_values():
    print("### RETURN VALUE UNIQUENESS")

    y = return_immutable()
    z = return_immutable()
    print("Returned immutables are", "" if y is z else "not", "unique")

    y = return_mutable()
    z = return_mutable()
    print("Returned mutables are", "" if y is z else "not", "unique")


# ===================================================================================================================== #

def ref_counting():
    print("### REFERENCE COUNTING")
    x = ["some value"]
    y = x

    print("Ref counts of local variables")
    print(x is y)  # True: x and y are only different names for the same object (["some value"])
    print(sys.getrefcount(x))  # Three references to the object:
    print(sys.getrefcount(y))  # x, y, and the local variable in sys.getrefcount
    print()

    print("Ref counts of local variables after materializing the locals dict")
    print(sys.getrefcount(
        locals()['x']))  # This materializes the dict, which adds two extra mentions of the object => output 5
    print(sys.getrefcount(x))  # The dict now exists and continues to do so until we leave the function.
    print(sys.getrefcount(y))  # Hence, these two lines will now output 5 as well.
    print()

    print("All variables in the test are actually the same object:")
    print(x is y is locals()['x'] is locals()['y'])  # all the objects actually are the same
    print()

    print("Ref counts of literals")
    print(sys.getrefcount(1))  # 122 references: There are a lot of objects with value 1 somewhere in the system
    print(sys.getrefcount(1.0))  # 2 -- I honestly don't understand this one -- it's 2 for every float
    print(sys.getrefcount([1]))  # directly bind the newly created mutable object [1] to the argument of getrefcount
    print()


# ===================================================================================================================== #

def main():
    is_and_equals()
    return_values()
    ref_counting()


if __name__ == '__main__':
    main()
