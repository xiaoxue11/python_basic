def set_level(level_num):
	def set_func(func):
		def call_func(*args, **kwargs):
			if level_num == 1:
				print('------just test1-----')
			elif level_num == 2:
				print('------just test2-----')
			return func(*args, **kwargs)
		return call_func
	return set_func


@set_level(1)
def test(*args, **kwargs):
	print('----1-------')
	return args,kwargs

print(test(5,6,7,aa='123'))
