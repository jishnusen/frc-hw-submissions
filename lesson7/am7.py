def l1():
	print("Carl Csaposs - 15")
	print("Months: " + str(15*12))

def l1_input(name, age):
	print(name + " - " + age)
	print("Months: " + str(age*12))

def l2():
	name = raw_input("Enter your name: ")
	num = raw_input("How many pizzas? ")
	pep = raw_input("How many pepperonis? ")
	olv = raw_input("How many olives? ")
	print(name + " ordered " + num + " pizzas with " + pep + "pepperonis and " + olv + " olives.")

def l2_input(name, num, pep, olv):
	print(name + " ordered " + num + " pizzas with " + pep + "pepperonis and " + olv + " olives.")

def l3():
	print(float(4.6), int(4.6))
	print(int(3.7))
	#print(int("4.5"))
	#print(int(" 4 and 5"))
	#print(float("three point six"))
	#print(float("three"))

def l4():
	age = raw_input("What is your age? ")
	if age >= 35:
		lvl = 5
	elif age >= 21:
		lvl = 4
	elif age >= 18:
		lvl = 3
	elif age >= 16:
		lvl = 2
	elif age >= 14:
		lvl = 1
	else:
		lvl = 0
		print("You don't meet any requirements.")

	list1 = ["You can join the robotics team.", "You can drive and get a job.", "You are an adult.", "You can drink.", "You can run for president."]

	print("")

	for var1 in range(0, lvl):
		print(list1[var1])

def l4_input(age):
	if age >= 35:
		lvl = 5
	elif age >= 21:
		lvl = 4
	elif age >= 18:
		lvl = 3
	elif age >= 16:
		lvl = 2
	elif age >= 14:
		lvl = 1
	else:
		lvl = 0
		print("You don't meet any requirements.")

	list1 = ["You can join the robotics team.", "You can drive and get a job.", "You are an adult.", "You can drink.", "You can run for president."]

	print("")

	for var1 in range(0, lvl):
		print(list1[var1])

def l5A():
	lista = ["a", "an", "at", "aa", "arc", "all", "as", "and", "in", "it"]
	word = raw_input("Please enter a word: ")

	cont = True
	for var1 in range (0,9):
		if word == lista[var1]:
			cont = False

	if cont == False:
		print("no")
	else:
		lista.append(word)
		print("done.")
	print(lista)

def l5A_input(lista, word):
	cont = True
	for var1 in range (0,9):
		if word == lista[var1]:
			cont = False

	if cont == False:
		print("no")
	else:
		lista.append(word)
		print("done.")
	print(lista)

def l5B():
	name = raw_input("Name: ")
	color = raw_input("Favorite color? ")
	petn = raw_input("Number of pets: ")
	ar1 = [name, color, petn]

	print(ar1[0] + "'s favorite color is " + ar[1] + ". They have " + ar[2] + " pets.")

def l5B_input(ar1):
	print(ar1[0] + "'s favorite color is " + ar[1] + ". They have " + ar[2] + " pets.")

def l6():
	cont = True
	ar1 = []
	while cont == True:
		inp = raw_input("Type 'stop' to stop ")
		if inp == "stop" or inp == "Stop":
			return
		else:
			ar1.append(inp)

def l6_input(inp):
	#cont = True # Define as global outside of func
	#ar1 = [] # Define as global outside of func
	while cont == True:
		if inp == "stop" or inp == "Stop":
			return
		else:
			ar1.append(inp)

def l6B():
	ar1 = [1,2,3,4,5]
	ar1.reverse()

def l6B_input(ar1):
	ar1.reverse()





