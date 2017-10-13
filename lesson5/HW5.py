
cocobeans = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

petshop= []


word= raw_input ("Give me a word: ")

if word in cocobeans:
	print "word in array"
else:
	print "Not in the array, adding it now... added"
	cocobeans.append(word)
print len(cocobeans)
print cocobeans


print ""
print""

name=raw_input("What is your name? ")
petshop.append(name)
color=raw_input("What is your favorite color? ")
petshop.append(color)
numofpets=raw_input("How many pets do you have? ")
petshop.append(numofpets)

print petshop[0] + "'s favorite color is " + petshop[1] + " and they have" , petshop[2] , "pets."