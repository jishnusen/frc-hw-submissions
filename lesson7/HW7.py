cocobeans = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
petshop= []
array = []



def HW1 ():
	print "Kate Unger"
	print 13 * 12

	print ""
	print ""
	return

def HW2 ():
	name=raw_input("What is your name? ")
	num_pizza=raw_input(" How many pizzas? ")
	pepe=raw_input("Out of those, how many do you want to have pepperoni? ")
	olive=raw_input("What about olives? ")
	print name + " ordered " + num_pizza + " pizzas with " + pepe + " pepperonis and " + olive + " olives."

	print ""
	print ""
	return

def HW4():
	
	age = int(raw_input("Your age? "))
	
	if age < 14:
		print "Sorry, you can't do anything... yet!"
	elif age >= 14 and age < 16:
		print "You can join the awesome 1678 team! "
	elif age >= 16 and age < 18:
		print "You can join the awesome 1678 team! "
		print "You can drive and get a job!"
	elif age >=18 and age <21:
		print "You can join the awesome 1678 team! "
		print "You can drive and get a job!"
		print "You can attend college"
	elif age >= 21 and age <35:
		print "You can join the awesome 1678 team! "
		print "You can drive and get a job! "
		print "You can attend college! "
		print "You are an adult! "
	else:
		print "You can join the awesome 1678 team! "
		print "You can drive and get a job"
		print "You can attend college! "
		print "You are an adult! "
		print "You can become president! "

	print ""
	print ""

	return

def HW5():
	word= raw_input ("Give me a word: ")

	if word in cocobeans:
		print "word in array"
	else:
		print "Not in the array, adding it now... added"
		cocobeans.append(word)
	print len(cocobeans)
	print cocobeans


	print ""

	name=raw_input("What is your name? ")
	petshop.append(name)
	color=raw_input("What is your favorite color? ")
	petshop.append(color)
	numofpets=raw_input("How many pets do you have? ")
	petshop.append(numofpets)

	print petshop[0] + "'s favorite color is " + petshop[1] + " and they have" , petshop[2] , "pets."

	print ""
	print ""

	return

def HW6():
	inputs = ""

	while inputs != "stop" and inputs != "Stop":
		inputs = raw_input("What do you want to put in the array? (type 'stop' to stop) ")

		if inputs != "stop" and inputs != "Stop":
			array.append(inputs)
	print array

	print ""

	return

HW1()
HW2()
HW4()
HW5()
HW6()


ef isitdivis(firstnum, secnum):
	if firstnum % secnum == 0:
		print "It is divisible"
	else:
		print "it is not divisible :("

a = int (raw_input("Number: "))
b = int (raw_input ("Number: "))

isitdivis(a,b)

