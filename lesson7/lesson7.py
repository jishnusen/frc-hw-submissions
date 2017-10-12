def lesson1():
	name = raw_input("What is your name: ")

	age = raw_input("What is your age: ")

	ageMonths = int(age)  * 12

	print "Hi " + name + ", you are " + str(age) +  " years old. You are " + str(ageMonths) + " months old."

def lesson2():
	name = str(raw_input("What is your name?"))

	pizza = int(raw_input("How many pizzas would you like?"))

	olives = int(raw_input("How many olives would you like?"))

	pepperoni = int(raw_input("How many pieces of pepperoni would you like?"))

	print "Hi, " + name + ", you ordered " + pizza + " pizzas with " + olivies + " olives and " + pepperoni + " pepperonis."

def lesson4():
	age = int(raw_input("Please enter your age.  "))

	if age > 13:
	    print"You can join the robotics team."
	else:
	    print"You are not old enough to join the robotics team"

	if age > 15:
	    print"You are allowed to drive and a job"
	else:
	    print"You are too young to drive and to get a job"

	if age > 17:
	    print"You can attend college"
	else:
	    print"You can't attend college"

	if age > 20:
	    print"You are an adult"
	else:
	    print"You are not an adult"

	if age > 34:
	    print"You are eligible to be president"
	else:
	    print"You are not eligible to be president"

def lesson5():
	wordArray = ["joe", "ham", "sid", "alex", "seven", "array", "pizza", "hombre", "lesson", "people"]
	wordInput = raw_input("Enter a word: ")

	if wordInput in wordArray:
		print "This word is alread a part of this array."
	else:
	        wordArray.append(wordInput)
	        print wordArray

def lesson5number2():
	name = raw_input("What is your name? ")
	color = raw_input("What is your favorite color? ")
	pet = raw_input("How many pets do you have? ")
	array = [name, color, pet]
	print array[0] + "'s favorite color is " + array[1] + ". They have " + array[2] + " pets."

def lesson6():
	x = 1
	array = []
	while x == 1:
		userInput = raw_input("Enter a word: ")
		if userInput == "stop":
			x = 10
			print array
		else:
			array.append(userInput)

def lesson6number2():
	array = [1,2,3,4,5,6]
	print array
	array2 = []
	for i in reversed(array):
		array2.append(i)
	print array2