def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)


def duplicate_encode(word):
	#your code here
	d1 = {}
	s1 = []
	for i in word:
		temp = i.lower()
		d1[temp]=d1.get(temp,0)+1

	for j in word:
		temp = j.lower()
		if d1.get(temp)>1:
			s1.append(')')
		else:
			s1.append('(')
	return ''.join(s1)


if __name__ == '__main__':
	outer()
	ret = duplicate_encode('Success')
	print(ret)
	print(type(ret))