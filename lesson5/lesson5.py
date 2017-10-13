import time
lst = ["a","b","c","d","e","f","g","h","i","j"]
letter = raw_input("Enter any letter in the alphabet:\n")
if letter in lst:
	print "Your letter was in my list!"
else: 
	letter += "<-- Your letter"
	lst.append(letter)
	print "We added your letter to our list!"
for letters in lst:
	print letters
	time.sleep(0.2)

#Assignment Number 2:

name = raw_input("What's your name?\n")
time.sleep(0.3)
color = raw_input("What's your favorite color?\n")
time.sleep(0.3)
pets = raw_input("How many pets do you have?\n")
time.sleep(0.5)
print name + "'s favorite color is " + color + " and " + name + " has " + pets + " pets!"