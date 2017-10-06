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