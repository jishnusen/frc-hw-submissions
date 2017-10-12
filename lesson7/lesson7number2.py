def divisble(x,y):
	div = float(x)/y
	boolean1 = div.is_integer()
	if boolean1 == True:
		print "These numbers are divisble"
	else:
		print "These numbers not are divisble"

divisble(float(raw_input("Enter a number: ")), float(raw_input("Enter a number: ")))
