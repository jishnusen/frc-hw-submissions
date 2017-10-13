#lesson 1 homework
def printnameandage():
	print("Jason 13")
	print(13*12)
printnameandage()

#lesson2 homework
def pizza(x,y,z):
	name = raw_input("What is your name?")
	print(name + " ordered " + x +" pizzas with "+ y + " peppornis and "+ z + " olives ")

x = raw_input("How many pizzas would you like?")
y = raw_input("How many peppornis would you like?")
z = raw_input("How many olives would you like?")

pizza(x,y,z)

#lesson 4 homework
def rights(age):
	if age > 14:
		print("You can join the robotics team.")
	else:
		print("You cannot join the robotics")

	if age > 16:
		print("You can get a job and drive.")
	else:
		print("You cannot drive and get a job")

	if age > 18:
		print("You can attend college.")
	else:
		print("You cannot attend college.")

	if age > 21:
		print("You are an adult.")
	else:
		print("You are not an adult.")

	if age > 35:
		print("You can become president.")
	else:
		print("You cannot become president")

age= int(raw_input("How old are you"))

rights(age)


#lesson 5
def wordlist(word,userword):
	
	if userword in words:
		print("Your word is in my list of ten words")
	else:
		words.append(userword)
	print words

words = ["one","two","three","four","five","six","seven","eight","nine","ten"]
userword=raw_input("Give me a word.")
wordlist(words,userword)

#lesson 6
def listofwords(x,words):
	x = ""
	words=[]
	value = False
	while value == False:
		x = raw_input("Input a word\n")
		if x == "stop":
			value = True
		else:
			words.append(x)
	print words
x = raw_input("Input a word\n")
words=[]
listofwords(x,words)


