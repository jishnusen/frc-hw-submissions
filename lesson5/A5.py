a = "pizza"
b = "popcorn"
c = "peaches"
d = "pears"
e = "pasta"
f = "peas"
g = "pepperoni"
h = "potato"
i = "potato chips"
j = "Pepsi"

array = [a, b, c, d, e, f, g, h, i, j]

food = raw_input("Enter a food that starts with 'p'. ")

if food in array:
	print food + " is/are on the list. "
else:
	print "Sorry, " + food + " is/are not on the list. "

a = raw_input("What is your name? ")
b = raw_input("What is your favorite color? ")
c = int(raw_input("How many pets do you have? "))

array = [a, b, c]

print array[0] +"'s favorite color is " + array[1] +". " 

if array[2] == 1:
	print "Also, " + array[0] + " owns " + str(array[2]) + " pet."
else: 
	print "Also, " + array[0] + " owns " + str(array[2]) + " pets."