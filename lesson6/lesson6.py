import time
#1

print "Welcome to my list!"
lst = []
value = False
while value == False:
	variable = str(raw_input("Enter any word!\n"))
	if variable == "stop":
		print lst
		value = True
	else: 
		lst.append(variable)
		

#2

print "Welcome to my list! (pt2)"
lstTwo = []
wordOne = raw_input("Enter any word\n")
if len(wordOne) > 0:
	lstTwo.append(wordOne)
wordTwo = raw_input("Enter another word!\n")
if len(wordTwo) > 0:
	lstTwo.append(wordTwo)
wordThree = raw_input("Enter another word!\n")
if len(wordThree) > 0:
	lstTwo.append(wordThree)
wordFour = raw_input("Enter another word!\n")
if len(wordFour) > 0:
	lstTwo.append(wordFour)
wordFive = raw_input("Enter another word!\n")
if len(wordFive) > 0:
	lstTwo.append(wordFive)
print "This is your list right now:\n"
for i in lstTwo:
	time.sleep(0.2)
	print i
	time.sleep(1)
print "This is your list backwards:\n"
for x in reversed(lstTwo):
	time.sleep(0.2)
	print x

