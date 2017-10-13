useIn = raw_input("Please input a word to add to a list: ")
list1 = [useIn]
while useIn != "stop":
	useIn = raw_input("Please input a word to add to a list: ")
	if useIn == "stop":
		print list1
	else:
		list1.append(useIn)