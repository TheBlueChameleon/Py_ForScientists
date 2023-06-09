import functools
import timeit


def use_join(data):
    return "".join(data)


def concatenator(acc, elm):
    return acc + elm


def use_functools(data):
    return functools.reduce(concatenator, data, "")


def use_for(data):
    result = ""
    for elm in data:
        result += elm
    return result


def main():
    data = [f"String {i}|" for i in range(2)]

    variables = globals().copy()
    variables.update(locals())

    print(timeit.timeit("use_join(data)", globals=variables))
    print(timeit.timeit("use_for(data)", globals=variables))
    print(timeit.timeit("use_functools(data)", globals=variables))


if __name__ == '__main__':
    main()
