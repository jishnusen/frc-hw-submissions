warray = []
word = raw_input("Enter word")
while word:
	warray.append(word)
	word = raw_input("Enter word")
	if word == "stop":
		print "STOPPED"
		print warray