def divNum(a, b):
	c = a% b
	if c == 0:
		print "It is divisible"
		div = a / b 
		print div
		return True
	else:
		print "It's not divisible"
		return False
a = int(raw_input("Enter the first number:"))
b = int(raw_input("Enter the second number:"))
divNum(a, b)