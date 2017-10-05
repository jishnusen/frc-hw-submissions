array = ["Hello", "Yay", "Happy", "Array", "Word", "Number", "Emu", "Whale", "Narwhal", "Fun"]
a = raw_input("Please enter a word")
if a in array:
	print "That word is already in the array. Congratulations."
else:
	array.append(a)
	print array 
