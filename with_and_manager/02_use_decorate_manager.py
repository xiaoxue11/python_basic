from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    file = open(path, mode)
    yield file
    file.close()


if __name__ == '__main__':
    with my_open('2.txt', 'w') as f:
        f.write('hello, world!')
