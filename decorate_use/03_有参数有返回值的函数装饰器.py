def set_func(func):
	def call_func(*args, **kwargs):
		print('------just test-----')
		return func(*args, **kwargs)
	return call_func

@set_func
def test(*args, **kwargs):
	print('----1-------')
	return args,kwargs

print(test())
print(test(3))
print(test(3,4))
print(test(5,6,7,aa='123'))
