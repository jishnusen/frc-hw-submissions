words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
newword = raw_input("what word")
if newword == "one" or newword == "two" or newword == "three" or newword == "four" or newword == "five" or newword == "six" or newword == "seven" or newword == "eight" or newword == "nine" or newword == "ten":
	print "already in"
else:
	words.append(newword)

print words

array = [raw_input("name?"), raw_input("fav color?"), raw_input("how many pets?")]
print array[0] + "'s favorite color is " + array[1] + ". They have " + array[2] + " pets."