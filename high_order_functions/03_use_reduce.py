from functools import reduce


def add(x, y):
    return x + y


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    # reduce(funct,iterable[, initial])
    b = reduce(add, a)
    print(b)
    c = reduce(add, a, 6)
    print(c)
