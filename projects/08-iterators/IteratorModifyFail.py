def incomplete_filter():
    data = [2, 3, 5, 7, 8, 10, 11]

    for i, num in enumerate(data):
        if num % 2 == 0:
            print("removing", num, "at index", i)
            del data[i]

    print(data)
    print(10 in data)


def add_fail():
    data = {1, 2, 3}

    try:
        for num in data:
            if num % 2 == 1:
                data.add(2 * num)
    except RuntimeError as e:
        print("Operation failed:", e)


def main():
    incomplete_filter()
    add_fail()


if __name__ == '__main__':
    main()
