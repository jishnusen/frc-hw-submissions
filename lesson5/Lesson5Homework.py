print "1."
words = ["hi", "banana", "kiwi", "axiom", "blobfish", "David", "Carlip", "papaya", "pineapple", "autocannibalistic"]
x = raw_input("Try to guess a word on my list! ")
if x in words:
	print "Wow! You must be psychic! That was one of my words!"
else:
	print "Uh... Nope! That wasn't one of my words... But it is now!"
	words.append(x)
print words

print " "
print "2."
name = raw_input("What's your name? ")
color = raw_input("What's your favorite color? ")
x = raw_input("How many pets do you have? ")
array = [name, color, x]
print array[0] + "'s favorite color is " + array[1] + "."
if "1" in array:
	print "They have one pet."
else:
	print "They have " + array[2] + " pets."