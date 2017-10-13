num1 = int(raw_input("Enter a number."))
num2 = int(raw_input("Enter a second number."))
def divisible(a,b):
	if num1 % num2 == 0 :
		print True
	else:
		print False
divisible(num1, num2)