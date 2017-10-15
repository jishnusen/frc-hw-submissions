def rectangle():
	for i in range(3):
		print "0" + "0" + "0" + "0" + "0"

def plzStop():
	list1 = []
	useIn = raw_input("Please input a word to add to a list: ")
	while useIn != "stop":
		if useIn == "stop":
			print list1
		else:
			list1.append(useIn)



def divisible(a, b):
	x = float(a/b)
	y = a/b
	if x != y:
		return True
	else:
		return False


def listTest():
	array1 = ['Yeet', 'float', 'Dang', 'CSGO', 'Arma', ';)', 'Hi', 'Eight', 'Square', '100']
	word1 = raw_input("Please input your fave word yo! ")
	if word1 in array1:
		return "Sorry fam, we are broskis now m8."
	else:
		array1.append(word1)
		return array1

def rules():
	userAge = int(raw_input("How old are you? "))

	if userAge >= 14:
		print "Congradulations, you can now join the prestigous robotics team, Citrus Circuits!"
		if userAge >= 16:
			print "You may also legally drive and work for wages!"
			if userAge >= 18:
					print "As well as Go to college!"
					if userAge >= 21:
						print "AND drink and smoke! (even though you should avoid both in excess.)"

def info():
	name = raw_input("What is your name? ")
	pets = raw_input("How many pets do you have? ")
	color = raw_input("Favorite color? ")
	array2 = [name, pets, color]
	print (array2[0]+ "'s favorite color is " +array2[1]+ ". They have " + array2[2] + " pets.")

def pizzatype(name, pizzas, pepperoni, olives):
		print (name +" wants to order " + pizzas +" pizzas with " + pepperoni + " slices of pepperoni and "+ olives+ " olives.")

def average(num1, num2, num3):
	return float((num1 + num2 + num3)/3)
def self():
	return ("Hi, My name is Zach Callahan. I am 15 years old. That comes out to about " + str(15*12) +" months.")