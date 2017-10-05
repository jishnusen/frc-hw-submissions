array = []
while True:
	word = raw_input("word?")
	if word != "stop":
		array.append(word)
	else:
		print array
		break