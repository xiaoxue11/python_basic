def get_score(score):
    return score > 75


if __name__ == '__main__':
    a = [20, 50, 90, 69, 89, 80]
    # filter(func, iterable)
    b = list(filter(get_score, a))
    print(b)
    c = list(filter(lambda x: x > 75, a))
    print(c)
