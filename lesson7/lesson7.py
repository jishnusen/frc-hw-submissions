def lesson1():
	print "Hanson"
	age = 15
	print age
	print age * 12

def lesson2():
	name = raw_input("What is your name?")
	x = int(raw_input("how many pizzas do you want?"))
	y = int(raw_input("how many pieces of pepperoni?"))
	z = int(raw_input("how many olives?"))
	print name + " ordered " + str(x) + " pizzas with " + str(y) + " pepperonis and " + str(z) + " olives."

	avg = (x + y + z) / 3

	print "challenge: " + str(avg)

def lesson4():
	age = int(raw_input("what is your age?"))
	if age >= 35:
		print "you can join the robotics team"
		print "you can drive and get a job"
		print "you can attend college"
		print "you are an adult"
		print "you can become President"
	elif age >= 21:
		print "you can join the robotics team"
		print "you can drive and get a job"
		print "you can attend college"
		print "you are an adult"
	elif age >= 18:
		print "you can join the robotics team"
		print "you can drive and get a job"
		print "you can attend college"
	elif age >= 16:
		print "you can join the robotics team"
		print "you can drive and get a job"
	elif age >= 14:
		print "you can join the robotics team"

def lesson5():
	words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
	newword = raw_input("what word")
	if newword == "one" or newword == "two" or newword == "three" or newword == "four" or newword == "five" or newword == "six" or newword == "seven" or newword == "eight" or newword == "nine" or newword == "ten":
		print "already in"
	else:
		words.append(newword)

	print words

	array = [raw_input("name?"), raw_input("fav color?"), raw_input("how many pets?")]
	print array[0] + "'s favorite color is " + array[1] + ". They have " + array[2] + " pets."

def lesson6():
	array = []
	while True:
		word = raw_input("word?")
		if word != "stop":
			array.append(word)
		else:
			print array
			break

def lesson7(a, b):
	if a % b == 0:
		print "divisible."
		return True
	else:
		print "not divisible."
		return False
		

