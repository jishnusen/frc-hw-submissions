
def Divide(a,b): 
 if a % b == 0:
   	print "These numbers are divisible."
 else:
   	print "These numbers are not divisible"

yay = int(raw_input("Choose a number: "))
woot = int(raw_input("Choose another number:"))

Divide(yay,woot)

print ""
print ""

#Lesson 1
def NameAge():
	print "Ellie"
	print "13"

def AgeMonths(a):
	print a * 12
NameAge()
AgeMonths(13)

#Lesson 2
def Pizza():
	name = raw_input("What is your name?")
	num = raw_input("How many pizzas would you like?")
	pep = raw_input("How many pepperonis would you like?")
	olive = raw_input("How many olives would you like?")
	print name + " ordered " + num + " pizzas with " + pep + " pepperonis and " + olive + " olives."

Pizza()

#Lesson 4
def TellAge(age):
	if age < 13:
		print "You are too young to join Citrus Circuits"
	elif age >= 13 and age < 16:
		print "Congratulations, you can join Citrus Circuits"
	elif age >= 16 and age < 18:
		print "Congratulations, you can drive. Dont die."
	elif age >= 18 and age < 21:
		print "Congratulations, you can go to college and vote."
	elif age >= 21 and age < 35:
		print "Congratulations, you can run for president and stuff."

age = int(raw_input("How old are you?"))
TellAge(age)

#Lesson 5-1
def Array():
	array = ["Hello", "Yay", "Happy", "Array", "Word", "Number", "Emu", "Whale", "Narwhal", "Fun"]
	a = raw_input("Please enter a word")
	if a in array:
		print "That word is already in the array. Congratulations."
	else:
		array.append(a)
		print array 
Array()

#Lesson 6-1
def Cactus():
		cactus = []
	a = raw_input("Enter a word")
	while a != "stop":
		a = raw_input("Enter a word")
		cactus.append(a)

Cactus()

#Lesson 6-2
def BackArray
	cactus = ["red", "orange", "yellow", "green", "blue", "purple"]
	print cactus
	a = len(cactus)
	cactus2 = []
	cactus2.append(cactus[5])
	cactus2.append(cactus[4])
	cactus2.append(cactus[3])
	cactus2.append(cactus[2])
	cactus2.append(cactus[1])
	cactus2.append(cactus[0])
	print cactus2
BackArray()
	






