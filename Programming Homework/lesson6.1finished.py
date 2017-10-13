def divNum(a, b):
	c = a % b
	if c == 0:
		print "It's divisible"
		div = a / b
		print div
		return True
	else:
		print "It's not divisible"
		return False
a = int(raw_input("enter the first number"))
b = int(raw_input("enter the sencond number:"))
divNum(a, b)