def assignment1(a, b, c):
	print a
	print b
	print c
assignment1("Laura", 17, (17*12+1))

def assignment2part1():
	a = raw_input("What is your name? ")
	b = raw_input("How many pizzas do you want? ")
	c = raw_input("How many pepperonis do you want? ")
	d = raw_input("How many olives do you want? ")
	print a + " ordered " + str(b) + " with " + str(c) + " pepperonis and " + str(d) + " olives. "

assignment2part1()

def assignment2part2():
	a = float(raw_input("Enter a number. "))
	b = float(raw_input("Enter a second number. "))
	c = float(raw_input("Enter a third number. "))
	print str((a+b+c)/3) + " is the average of " + str(a) + ", " + str(b) + ", and " +str(c)

assignment2part2()


def assignment4 ():
	age = int(raw_input("How old are you? "))
	if age >= 14 and age < 16:
		print "You can join the robotics team" 
	elif age >= 16 and age < 18:
		print "You can join the robotics team, and get a drivers lisence"
	elif age >=18 and age < 21:
		print "You can join the robotics team, get a lisence, and go to college"
	elif age >= 21 and age < 35:
		print "You can join the robotics team, get a lisence." 
		print "You can go to college, and you are an adult"
	elif age >= 35:
		print "You can join the robotics team, get a lisence."
		print "You can go to college, you are an adult."
		print "and become president."
	elif age < 14 and age >= 0:
		print "You are too young to do anything"
	else:
		print "You did not follow directions"
assignment4()


def assignment5(a,b,c,d,e,f,g,h,i,j):
	array = [a, b, c, d, e, f, g, h, i, j]
	z = raw_input("Enter a food that starts with 'p'. ")
	if z in array:
		print z + " is/are on the list. "
	else:
		print "Sorry, " + z  + " is/are not on the list. "

assignment5("pizza", "popcorn", "peaches", "pears", "pasta", "peas", "pepperoni", "potato", "popato chips", "Pepsi")


def assignment5part2 (a,b,c):
	array = [a, b, c]
	print array[0] +"'s favorite color is " + array[1] +". " 
	if array[2] == 1:
		print "Also, " + array[0] + " owns " + str(array[2]) + " pet."
	else: 
		print "Also, " + array[0] + " owns " + str(array[2]) + " pets."

name = raw_input("What is your name? ")
color = raw_input("What is your favorite color? ")
pet = int(raw_input("How many pets do you have? "))
assignment5part2(name, color, pet)

def assignment6part1(input):
	array = []
	while input != "Stop":
		input = raw_input("Enter Something. ")
		array.append(input)
	if input == "Stop":
		for i in range(0, len(array)-1):
			print array[i]
assignment6part1(input)

def assignment6part2():
	array2 = ["Laura", "Dog", "Grapes"]
	reverse = []
	for i in range(0, len(array2)):
		reverse.append(array2[len(array2)- 1 - i])
		if (len(array2) -1 -i) == 0:
			print reverse
assignment6part2()

