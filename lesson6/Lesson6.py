array = []
word = "" 
print("PLease enter a word the amount of times you would like it to be added to a list to finish input stop ")
while word != "stop":
    word = raw_input("Give me a word: ")
    if word != "stop":
       array.append(word)
print array
print "Your list has " + str(len(array)) + " words in it!"
