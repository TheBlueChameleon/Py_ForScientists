import typing


class Collatz:
    def __init__(self, n: int):
        self.n = 2 * n

    def __iter__(self) -> typing.Iterator:
        return self

    def __next__(self) -> int:
        if self.n % 2 == 0:
            self.n = self.n // 2
        else:
            if self.n == 1:
                raise StopIteration
            self.n = 3 * self.n + 1

        return self.n

def main():
    print("Collatz Sequences, generated by class:")
    print("  C8:", [num for num in Collatz(8)])
    print("  C9:", [num for num in Collatz(9)])
    print("  max(C9):", max(Collatz(9)))


if __name__ == '__main__':
    main()

def main():
    print("Collatz Sequences, generated by class:")
    print("  C8:", [num for num in Collatz(8)])
    print("  C9:", [num for num in Collatz(9)])
    print("  max(C9):", max(Collatz(9)))


if __name__ == '__main__':
    main()