wordArray = ["joe", "ham", "sid", "alex", "seven", "array", "pizza", "hombre", "lesson", "people"]
wordInput = raw_input("Enter a word: ")

if wordInput in wordArray:
	print "This word is alread a part of this array."
else:
        wordArray.append(wordInput)
        print wordArray
