import functools


def login_required(func):
    print("This is a change")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """This is a decorator inner"""
        return func(*args, **kwargs)

    return wrapper


def test1():
    """This is a test program"""
    print('This is a test1')


@login_required
def test2():
    """This is a test2 program"""
    print('This is a test2')


if __name__ == '__main__':
    print(test1.__name__)
    print(test1.__doc__)
    print(test2.__name__)
    print(test2.__doc__)
