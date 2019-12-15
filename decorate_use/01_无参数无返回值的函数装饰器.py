def set_func(func):
	def call_func():
		func()
		print('------1------')
	return call_func

@set_func
def test():
	print('------2------')

test()
