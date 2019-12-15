class Celsius:

    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


if __name__ == '__main__':
	man = Celsius()
	# set temperature
	man.temperature = 37
	# get temperature
	print(man.temperature)
	# get degrees Fahrenheit
	print(man.to_fahrenheit())
