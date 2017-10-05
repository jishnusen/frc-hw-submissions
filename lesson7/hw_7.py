def numbers(a, b):
	return a%b

def answer(c, d):
	if numbers(c, d) == 0:
		print str(c) + " is divisible by " + str(d)
	else:
		print str(c) + " is not divisible by " + str(d)

print "Input two numbers and this code will tell you if it is divisible."

z = int(raw_input("Enter the larger number"))
x = int(raw_input("Enter the smaller number"))

answer(z,x)
