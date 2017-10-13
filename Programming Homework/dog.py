class Dog:
	fur_color = "golden"
	eye_color = "blue"
	age = 3
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
	def walk(self,dist):
		self.pos+= dist
my_dog = Dog("Freddy", 0)
my_dog.walk(5)
print my_dog.pos
