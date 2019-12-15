def func(x):
	return x*x


if __name__ == '__main__':
	num = [1,2,3,4,5]
	l1 = [1,2,3,4]
	# map(func, *iterable)
	ret = map(func, num)
	print(type(ret))
	# print(list(ret))
	# print(set(ret))
	# print(tuple(ret))
	a = list(map(lambda x:x*x, num))
	b = list(map(lambda x,y: x+y, num, l1))
	c = list(zip(num, l1))
	d = list(map(lambda x,y: (x,y), num, l1))
	print(c)
	print(d)
