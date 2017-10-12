a = ["1", "6", "4", "-5", "3"]
for f1 in range(0, 5):
	b = raw_input("Guess a number between 0 and 10")
	if b == "1" or b == "6" or b == "4" or b == "-5" or b == "3":
		print b, "is one of my numbers too."
	else:
		print "Nope"