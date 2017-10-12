x = 1
array = []
while x == 1:
	userInput = raw_input("Enter a word: ")
	if userInput == "stop":
		x = 10
		print array
	else:
		array.append(userInput)
