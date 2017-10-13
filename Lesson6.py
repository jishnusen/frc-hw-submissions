#Lesson 6: Loops
#1:
array3 = []
while word != "stop":
	word = raw_input("Enter a word: ") 
	if word != "stop":
		array3.append(word)
print array3
#2:
array4 = [1,2,3,4,5]
print array4
a = len(array4)
array5 = []
array5.append(array4[4])
array5.append(array4[3])
array5.append(array4[2])
array5.append(array4[1])
array5.append(array4[0])
print array5