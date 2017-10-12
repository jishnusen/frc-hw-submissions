def ModYeller(a = float(raw_input("Number?")), b = float(raw_input("Number?"))):
	if a % b == 0:
		print "You picked numbers divisible by each other."
	else:
		print "Your numbers", a, "and", b, "were not divisible by each other."
ModYeller()