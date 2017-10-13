word = raw_input("What is your word?")
word_words = ["dog", "cat", "bird", "purple", "book", "table", "marker", "computer", "shoe", "chairs"]
if word in word_words:
	print "we have your word"
else:
	print "we don't have your word"
word_words.append(word)
print word_words

