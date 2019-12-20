if __name__ == '__main__':
    numList = ['1', '2', '3', '4']
    print(numList)
    print(','.join(numList))
    numTuple = ('1', '2', '3', '4')
    print(','.join(numTuple))

    s1 = 'abc'
    s2 = '123'
    print(s1.join(s2))
    print(s2.join(s1))

    test = {'2', '1', '3'}
    print(", ".join(test))

    test = {'Python', 'Java', 'Ruby'}
    s = '->->'
    print(s.join(test))

    test = {'mat': 1, 'that': 2}
    s = '->'
    print(s.join(test))
