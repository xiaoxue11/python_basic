from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with my_open('2.txt','w') as f:
	f.write('hello, world!')