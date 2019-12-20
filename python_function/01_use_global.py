def add():
    print(c)


def test():
    global c
    c = c + 2
    print(c)


def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


if __name__ == '__main__':
    c = 1
    add()
    test()
    foo()
    print("x in main : ", x)
