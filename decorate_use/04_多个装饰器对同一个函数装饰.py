def set_func1(func):
    def call_func(*args, **kwargs):
        print('------just test1-----')
        return func(*args, **kwargs)

    return call_func


def set_func2(func):
    def call_func(*args, **kwargs):
        print('------just test2-----')
        return func(*args, **kwargs)

    return call_func


@set_func1
@set_func2
def test(*args, **kwargs):
    print('----1-------')
    return args, kwargs


if __name__ == '__main__':
    print(test())
    print(test(3))
    print(test(3, 4))
    print(test(5, 6, 7, aa='123'))
