#division
def division(num1,num2):
	value=num1%num2
	if value==0:
		print ("Your numbers are divisible.")
	else:
		print("Your numbers aren't divisible.")
		
num1=int(raw_input("Input a number\n"))
num2=int(raw_input("Input another number\n"))
division(num1,num2)