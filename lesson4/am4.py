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