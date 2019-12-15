def set_func(func):
	def call_func(*args, **kwargs):
		print('------just test-----')
		func(*args, **kwargs)
	return call_func

@set_func
def test(num, *args, **kwargs):
	print('------{}------'.format(num))
	print('------{}------'.format(args))
	print('------{}------'.format(kwargs))


test(3)
test(3,4)
test(5,6,7,aa='123')
