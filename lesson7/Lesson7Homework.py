print "2. Without modulus"
def Function():
	number = float(raw_input("Give me a number. "))
	number2 = float(raw_input("Give me another number. "))

	quotient = number/number2
	string = str(quotient)
	string2 = ""
	decimal = False

	for i in string:
		if i == ".":
			decimal = True
			string2 += ("0" + i)
		elif decimal:
			string2 += (i)
	remainder = float(string2)

	if remainder * number2 != 0.0:
		return False
	else:
		return True

print Function()

print ""
print "2. With modulus"
num = float(raw_input("Give me a number. "))
num2 = float(raw_input("Give me another number. "))
if num % num2 == 0:
	print "It's divisible!"
else:
	print "It's not divisble..."