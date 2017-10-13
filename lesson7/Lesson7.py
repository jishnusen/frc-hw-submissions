#Lesson 7: Functions
#1:
#Lesson 1:
def lesson1():
	print "Chiara Wu is" + 2*13 + "months old."
lesson1()
#Lesson 2:
def lesson2():
	name = raw_input("What is your name? ")
	num = int(raw_input("How many pizzas would you like? "))
	pepp = int(raw_input("How many pieces of pepperoni would you like on your pizza(s)? "))
	olive = int(raw_input("How many olives would you like on your pizza(s)? "))
	print name + " has ordered " + num + " pizzas; " + pepp + " pieces of pepperoni and " + olive + " olives on the pizzas."
lesson2()
#Lesson 4:
def lesson4():
	age = int(raw_input("How many years old are you? "))
	if age < 14:
		print "You can't do anything. Go play some more Mario Kart until you've reached puberty."
	elif age >= 14 and age < 16:
		print "You can join the Citrus Circuits robotics team!"
	elif age >= 16 and age < 18:
		print "You can join the Citrus Circuits robotics team!"
		print "You can now drive and get a job!"
	elif age >= 18 and age < 21:
		print "You can join the Citrus Circuits robotics team!"
		print "You can now drive and get a job!"
		print "You're not yet an adult but you can go to college (not that I think you will)."
	elif age >= 21 and age < 35:
		print "You can join the Citrus Circuits robotics team!"
		print "You can now drive and get a job!"
		print "You're not yet an adult but you can go to college (not that I think you will)."
		print "You're an adult now! Taxes! (yay)"
	else age >=35:
		print "You can join the Citrus Circuits robotics team!"
		print "You can now drive and get a job!"
		print "You're not yet an adult but you can go to college (not that I think you will)."
		print "You're an adult now! Taxes! (yay)"
		print "You can become President now! (Again, not that you will.)"
lesson4()
#Lesson 5:
def lesson5():
	array = [thing1, thing2, thing3, thing4, thing5, thing6, thing7, thing8, thing9, thing10]
	new = raw_input("Enter a number or word: ")
	if new in array:
		print "This is already in the arrayyyyy."
	else:
		array.append(new)
	print array
	array2 = []
	name = raw_input("What is your name? ")
	array2.append(name)
	color = raw_input("What is your favorite color? ")
	array2.append(color)
	pets = int(raw_input("How many pets do you own? "))
	array2.append(pets)
	print array2[0] + "'s favorite color is " + color + " and they own " + pets + " pets."
lesson5()
#Lesson 6:
def lesson6():
	array3 = []
	while word != "stop":
		word = raw_input("Enter a word: ") 
		if word != "stop":
			array3.append(word)
	print array3
	array4 = [1,2,3,4,5]
	print array4
	a = len(array4)
	array5 = []
	array5.append(array4[4])
	array5.append(array4[3])
	array5.append(array4[2])
	array5.append(array4[1])
	array5.append(array4[0])
	print array5
lesson6()
#2: 
def funcfunc():
	