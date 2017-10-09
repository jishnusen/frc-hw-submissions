def Lesson1():
	print "Emily Lin, 15"
	print str(12*15+5) + " months"

def Lesson2():
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

def Lesson4():
	print "Lesson 4"
	age = int(raw_input("Age, please! "))
	if age<0:
		print "Um... no... Just... no..."
	if age<5 and age>0:
		print "Wow... littluns get computers mighty early, don't they?"
		print "Back in my day..."
	if age<14 and age>4:
		print "GO AWAY CHILD! YOU HAVE NO RIGHTS!"
	if age>=14 and age<=18:
		print "So... you can join robotics now, which is cool! Psst... Join progamming, why donchya?"
	if age>=16:
		print "You can start driving, which is cool. I don't even have my permit yet. :("
	if age>=18:
		print "You're an adult! Is that a good thing?"
	if age>=21:
		print "You can drink now! If you really want to? I guess..."
	if age>=35:
		print "You can be President now! Not that you WILL be, but you CAN be!"
	if age>100:
		print "Um... no. Is it terrible to say I don't believe you? But hey, if it's true, I'm sorry, I mean no disrespect."
	if age>110:
		print "Nope."

def Lesson4_5():
	print "Lesson 4.5"
	patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
	def calculate_bmi(weight, height):
		return weight / (height ** 2)
	for patient in patients:
		weight, height = patient
		bmi = calculate_bmi(weight, height)
		print "Patient's BMI is: ", str(bmi)

def Lesson5():
	print "1."
	words = ["hi", "banana", "kiwi", "axiom", "blobfish", "David", "Carlip", "papaya", "pineapple", "autocannibalistic"]
	x = raw_input("Try to guess a word on my list! ")
	if x in words:
		print "Wow! You must be psychic! That was one of my words!"
	else:
		print "Uh... Nope! That wasn't one of my words... But it is now!"
		words.append(x)
	print words

	print " "
	print "2."
	name = raw_input("What's your name? ")
	color = raw_input("What's your favorite color? ")
	x = raw_input("How many pets do you have? ")
	array = [name, color, x]
	print array[0] + "'s favorite color is " + array[1] + "."
	if "1" in array:
		print "They have one pet."
	else:
		print "They have " + array[2] + " pets."

def Lesson6(a):
	print "1."
	print "Type 'stop' when you want to stop adding to the array."
	array = []
	while a != "stop":
		a = raw_input("What would you like to add to the array? ")
		array.append(a)
	for i in range(0, len(array) - 1):
		print array[i]

	print ""
	print "2."
	array2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "and", "z"]
	print array2
	print " "
	print array2[::-1]

	print ""
	print "3. Extra Challenge"
	print " "
	print "1."
	sum1 = 0
	for j in range(1000):
		if j % 3 == 0 or j % 5 == 0:
			sum1 += j
	print sum1

	print ""
	print "2."
	sum2 = 0
	for k in range(4000000):
		if k % 2 == 0:
			sum2 += k
	print sum2

	print ""
	print "3."

	import math
	factors = []
	allPrime = False
	def divisible(a,b):
		return a % b == 0

	def isPrime(num):
		prime = True
		for i in range(2,num):
			if divisible(num,i):
				prime = False
		return prime

	def findFactors(num):
		for i in range(2,int(math.sqrt(num))):
			if divisible(num,i):
				if isPrime(i):
					factors.append(i)

	findFactors(600851475143)
	print factors

Lesson1()
Lesson2()
Lesson4()
Lesson5()
Lesson6("go")