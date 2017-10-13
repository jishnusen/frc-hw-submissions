lista = ["a", "an", "at", "aa", "arc", "all", "as", "and", "in", "it"]
	word = raw_input("Please enter a word: ")

	cont = True
	for var1 in range (0,9):
		if word == lista[var1]:
			cont = False

	if cont == False:
		print("no")
	else:
		lista.append(word)
		print("done.")
	print(lista)