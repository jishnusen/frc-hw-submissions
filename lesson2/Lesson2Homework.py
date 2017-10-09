x = raw_input("How many pieces of pepperoni would you like? ")
y = raw_input("How many olives would you like? ")
print "Okay, here's what I got on your pizza:"

if x == "1":
	print "One piece of pepperoni."
else:
	print x + " pieces of pepperoni."

if y == "1":
	print "One olive."
else:
	print y + " olives."

z = raw_input("Now, what is your name? ")
print "Thank you, " + z + ", your pizza will be delivered shortly."

print " "
print "CHALLENGE"
print " "
x = float(raw_input("A number, please. "))
y = float(raw_input("Another, please. "))
z = float(raw_input("Last one! "))
print "Thank you!"
a = raw_input("Calculating average...")
print (x+y+z)/3