def divide(x, y):
	dividend = float(x/y)
	remainder = x % y
	return remainder	
a = float(raw_input("Enter a number. "))
b= float(raw_input("Enter another number. "))
z = divide(a,b)
if z == 0:
	print str(a) + " is divisible by " + str(b)
else: 
	print str(a) + " is not divisible by " + str(b)