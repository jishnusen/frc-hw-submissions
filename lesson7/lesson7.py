import time

#
#
time.sleep(1)
print "Lesson One:"
time.sleep(0.5)

#Lesson One:
def lessonOne():
	print "Teo"
	print "13"
	print 13 * 12
lessonOne()
#
#
time.sleep(1)
print "Lesson Two:"
time.sleep(0.5)

#Lesson Two:
def lessonTwo():	
	name = raw_input("que es tu nombre\n")
	pepperoni = raw_input("cuantos pepperonis quieres\n")
	olive = raw_input("cuantos olives\n")
	fresas = raw_input("cuantas fresas te quieres\n")
	print "entonces... te quieres " + pepperoni + " pepperonis, " \
	+ olive + " olives, y " + fresas + " fresas.."
lessonTwo()
#
#
time.sleep(1)
print "Lesson Four:"
time.sleep(0.5)

#Lesson Four:
def lessonFour():	
	age = int(raw_input("ur age pls\n"))
	if age >= 35: 
		print "you can b presidente del amuricas norte states unity"
		print "u can drive carro n get a trabajo"
		print "u can go to colegio"
		print "ur adulto"
		print "u can b en robot team"
	elif age >= 21:
		print "u can drive carro n get a trabajo"
		print "u can go to colegio"
		print "ur adulto"
		print "u can b en robot team"
	elif age >= 18:
		print "u can b en robot team"
		print "u can drive carro n get a trabajo"
		print "u can go to colegio"
	elif age >= 16:
		print "u can b en robot team"
		print "u can drive carro n get a trabajo"
	elif age >= 14:
		print "u can b en robot team"
	else:
		print "boi"
lessonFour()
#
#
time.sleep(1)
print "Lesson Five:"
time.sleep(0.5)

#Lesson Five
def lessonFive():
	lst = ["a","b","c","d","e","f","g","h","i","j"]
	letter = raw_input("Enter any letter in the alphabet:\n")
	if letter in lst:
		print "Your letter was in my list!"
	else: 
		letter += "<-- Your letter"
		lst.append(letter)
		print "We added your letter to our list!"
	for letters in lst:
		print letters
		time.sleep(0.2)

	#Assignment Number 2:

	name = raw_input("What's your name?\n")
	time.sleep(0.3)
	color = raw_input("What's your favorite color?\n")
	time.sleep(0.3)
	pets = raw_input("How many pets do you have?\n")
	time.sleep(0.5)
	print name + "'s favorite color is " + color + " and " + name + " has " + pets + " pets!"
lessonFive()
#
#
time.sleep(1)
print "Lesson Six"
time.sleep(0.5)

#Lesson Six
def lessonSix():
	#1

	print "Welcome to my list!"
	lst = []
	value = False
	while value == False:
		variable = str(raw_input("Enter any word!\n"))
		if variable == "stop":
			print lst
			value = True
		else: 
			lst.append(variable)
		

	#2

	print "Welcome to my list! (pt2)"
	lstTwo = []
	wordOne = raw_input("Enter any word\n")
	if len(wordOne) > 0:
		lstTwo.append(wordOne)
	wordTwo = raw_input("Enter another word!\n")
	if len(wordTwo) > 0:
		lstTwo.append(wordTwo)
	wordThree = raw_input("Enter another word!\n")
	if len(wordThree) > 0:
		lstTwo.append(wordThree)
	wordFour = raw_input("Enter another word!\n")
	if len(wordFour) > 0:
		lstTwo.append(wordFour)
	wordFive = raw_input("Enter another word!\n")
	if len(wordFive) > 0:
		lstTwo.append(wordFive)
	print "This is your list right now:\n"
	for i in lstTwo:
		time.sleep(0.2)
		print i
		time.sleep(1)
	print "This is your list backwards:\n"
	for x in reversed(lstTwo):
		time.sleep(0.2)
		print x
lessonSix()
#
#


