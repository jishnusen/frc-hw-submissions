randomWords = ["Bus", "Truck", "Mobile", "Water", "Bottle", "Key", "Hand", "Door", "Desk", "Mouse"]

userword = raw_input("Input a word(Please make it school appropriate).")
userword_capatalized = ""
userword_capatalized += userword[0].upper()
for i in range(1, len(userword)):
	userword_capatalized += userword[i]

if userword_capatalized in randomWords:
	print "Your word is on the string!"
else:
	randomWords.append(userword_capatalized)

print randomWords