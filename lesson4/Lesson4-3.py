print "Hello! What pet would you like to adopt"
a = raw_input("What pet?")
if a.lower() != "cat" and a.lower() != "cats":
	print "That desk will help you over there."
else:
	b = raw_input("What color?")
	c = raw_input("How big?")
	d = raw_input("indoor/outdoor?")
	e = float(raw_input("What's your yearly income."))
	if e < 18000:
		print "Unfortunately, you broke. No cat 4 u. No cat 5 v."
	else:
		f = float(raw_input("How big is your house, sqare feet?"))
		if f < 500:
			print "Unfortunately, you got teensy house. No cat 4 u. No cat 5 v."
		else:
			print "So you'd like a ", c, "cat with", b, "fur, that is an ", d, "personality. Cool, We'll see what we can find"	