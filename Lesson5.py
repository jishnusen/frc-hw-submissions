#Lesson 5: Arrays
#1:
array = [thing1, thing2, thing3, thing4, thing5, thing6, thing7, thing8, thing9, thing10]
new = raw_input("Enter a number or word: ")
if new in array:
	print "This is already in the arrayyyyy."
else:
	array.append(new)
print array
#2:
array2 = []
name = raw_input("What is your name? ")
array2.append(name)
color = raw_input("What is your favorite color? ")
array2.append(color)
pets = int(raw_input("How many pets do you own? "))
array2.append(pets)

print array2[0] + "'s favorite color is " + color + " and they own " + pets + " pets."