def test(n=1):
	if n>3:
		return 
	print(n)
	test(n+1)
test()

list1=['python', 'java', 'c++']
print(list(enumerate(list1, 2019)))

nums = [1, 2, 3]
str1 = ['a', 'b', 'c']
print(nums)
print(str1)