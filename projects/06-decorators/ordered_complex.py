import functools


@functools.total_ordering
class ordered_complex(complex):
    def __lt__(self, other):
        return abs(self) < abs(other)


def main():
    z1 = ordered_complex(1, 0)
    z2 = ordered_complex(0, 1)

    print(z1 < z2)
    print(z1 > z2)
    print(z1 == z2)
    print(z1 != z2)
    print(z1, z2)
