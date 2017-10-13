#Lesson 5 HW
#1

words = ["hello", "bye", "good", "bad", "warm", "cold", "high", "low", "near", "far"]
new_w = raw_input("Type a word.")

if new_w in words:
 	print "Your typed word exists in the array!"
else:
 	words.append(new_w)
 	print "Your word was added to the array!"

print words