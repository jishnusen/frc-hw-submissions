words = ["red", "blue", "green", "purple", "magenta", "great", "wonderful", "yay!", "koala", "hi"]
anything = raw_input("what's your favorite word?")

if (anything in words) == True:
	print "i like that word too"

else: 
	words.append(anything)

print words




