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
class Dalmation(Dog):
	fur_color = "spotted"
	eye_color = "black"
my_dalmation = Dog("Fido", 1)
print my_dalmation.age
my_dalmation.walk(3)
my_dalmation.pos