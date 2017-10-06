def assignment1():
	print "My name is Raiyan and my age is " + str(15 * 12) + " months"

def assignment21():
	name = raw_input("What is your name?")
	pizzas = raw_input("How many pizzas do you want?")
	pepperoni = raw_input("How many pieces of pepperoni do you want?")
	olives = raw_input("How many pieces of olives do you want?")

	print name + " ordered " + pizzas + " pizzas with " + pepperoni + " pepperonis and " + olives + " olives."

def assignment22():
	number1 = raw_input("What is your first number? ")
	number2 = raw_input("What is your second number? ")
	number3 = raw_input("What is your third numeber? ")

	print "The average of your numbers is: " + str((int(number1)+int(number2)+int(number3))/3)

def assignment4():
	age = int(raw_input("What's your age?\n"))

	if age >= 14:
		print "You can join robotics"
		if age >= 16:
			print "You can drive/work"
			if age >= 18:
				print "You can go to college"
				if age >= 21:
					print "You can drink/smoke"
					if age >= 35:
						print "You can become President"
	else:
		print "Your too young"

def assignment4_5():
	patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
	def calculate_bmi(weight, height):
		return weight / (height ** 2)
	for patient in range(len(patients)):
		weight, height = patients[patient]
		bmi = calculate_bmi(weight, height)
		print "Patient's BMI is:" + str(bmi)

def assignment51():
	randomWords = ["Bus", "Truck", "Mobile", "Water", "Bottle", "Key", "Hand", "Door", "Desk", "Mouse"]

	userword = raw_input("Input a word(Please make it school appropriate).")
	userword_capatalized = ""
	userword_capatalized += userword[0].upper()
	for i in range(1, len(userword)):
		userword_capatalized += userword[i]

	if userword_capatalized in randomWords:
		print "Your word is on the string!"
	else:
		randomWords.append(userword_capatalized)

	print randomWords

def assignment52():
	userinfo = [raw_input("What's your name?"), raw_input("What's your favourite color"), raw_input("How many pets do you have")]

	print userinfo[0] + "'s favourite color is " + userinfo[1] + ". They have " + userinfo[2] + " pets."

def assignment61():
	userWord = ""
	newArray = ["ice", "fire", "cold"]
	while userWord != "stop":
		userWord = raw_input("Type out a word(Make it school appropriate!)").lower()
		newArray.append(userWord)

	print newArray

def assignment62():
	array = ["Ice", "Fire", "Earth", "Air"]
	rev_array = []

	for i in range(1, len(array) + 1):
		rev_array.append(array[(i * -1)])

	print rev_array

