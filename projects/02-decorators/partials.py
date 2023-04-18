import functools

import numpy as np


def derivative(f, epsilon=1E-6):
    def wrapper(x):
        return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

    return wrapper


def f(x, y):
    r_squared = x * x + y * y
    return np.exp(-r_squared) * np.cos(np.sqrt(r_squared))


def main():
    fx = functools.partial(f, y=0)
    dfx = derivative(fx)

    # when removing parameters before the first one, explicit naming of the residual parameters is necessary
    fy = lambda t: functools.partial(f, x=0)(y=t)
    dfy = derivative(fy)

    print(dfx(1))
    print(dfy(2))


if __name__ == '__main__':
    main()
