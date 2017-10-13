sentence = ["low", "pee", "hi", "no", "me", "ok", "sprint", "you", "nine", "ten"]
word = raw_input("Please list a word ")
if word in sentence :
	print("That is one of my secret words too!")
else :
	sentence = ["low", "pee", "hi", "no", "me", "ok", "sprint", "you", "nine", "ten",str(word)]
	print sentence
