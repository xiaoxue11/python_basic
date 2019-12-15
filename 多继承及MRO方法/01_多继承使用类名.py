class Parent:
	def __init__(self, name):
		print('parent init function run')
		self.name = name
		print('parent init function end')

class Son1(Parent):
	def __init__(self, name, age):
		print('Son1 init function run')
		self.age = age
		Parent.__init__(self,name)
		print('Son1 init function end')

class Son2(Parent):
	def __init__(self, name, gender):
		print('Son2 init function run')
		self.gender = gender
		Parent.__init__(self, name)
		print('Son2 init function end')

class Grandson(Son1, Son2):
	def __init__(self, name, age, gender):
		print('GrandSon init function run')
		Son1.__init__(self, name, age)
		Son2.__init__(self, name, gender)
		print('GrandSon init function end')

gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)

print("******多继承使用类名.__init__ 发生的状态******\n\n")

