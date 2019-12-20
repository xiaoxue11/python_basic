class File:
    def __init__(self, filename, filemode):
        self.filename = filename
        self.filemode = filemode

    def __enter__(self):
        print('entering')
        self.f = open(self.filename, self.filemode)
        return self.f

    def __exit__(self, *args):
        print('exit')
        self.f.close()


if __name__ == '__main__':
    with File('1.txt', 'w') as f:
        print('writing')
        f.write('hello,python')
