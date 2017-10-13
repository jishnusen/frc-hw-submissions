#lesson 5

words = ["one","two","three","four","five","six","seven","eight","nine","ten"]
userword=raw_input("Give me a word.")
if userword in words:
	print("Your word is in my list of ten words")
else:
	words.append(userword)
print words