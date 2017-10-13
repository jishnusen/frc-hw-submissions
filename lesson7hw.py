def divNum(a, b):
	c = a % b
	if c == 0:
		print "It is divisible."
		div = a / b
		print div
		return True
	else:
		print "It is not divisible."
		return False

a = int(raw_input("enter a first number:"))
b = int(raw_input("enter your second number:"))

divNum(a, b)