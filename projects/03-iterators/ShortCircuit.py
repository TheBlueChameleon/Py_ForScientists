import time

say_A = lambda: print("A"); True
say_B = lambda: print("B"); True

quick_to_evaluate = lambda: False
slow_to_evaluate = lambda: time.sleep(2); False


def main():
    if say_A() or say_B():
        # Since say_A() returns True, we do not need to evaluate say_B() to get the result of the logical or.
        # True or [Anything] always gives True.
        # This means that we do not get any side effects of say_B().
        # ==> Best practice: keep your functions free of side effects. Do something and return none, or compute a value
        #     and do nothing else.
        pass
    print()

    a = say_A()
    b = say_B()
    if a or b:
        # If you HAVE TO trigger the side effects of both calls, you can resort to eager evaluation: store the results
        # of either call in a separate variable that is only LATER used in an or/and expression.
        pass
    print()

    if slow_to_evaluate() and quick_to_evaluate():
        pass
    else:
        print("Wasted time by failing to leverage short circuiting")

    if quick_to_evaluate() and slow_to_evaluate():
        pass
    else:
        print("Got the same result way faster")


if __name__ == "__main__":
    main()
