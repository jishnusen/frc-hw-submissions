var = raw_input("Enter any word you would like.")
words = ["Lucas", "is", "ur", "master", "and", "you", "cant", "do", "anything", "hahaha"]
if var in words:
	print "Word is all ready included in words."
else:
	print "Word not included, will be added."
	words.append(var)
print words