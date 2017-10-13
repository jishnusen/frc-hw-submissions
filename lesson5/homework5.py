
#The First Part of Assignment 5

array1 = ['Yeet', 'float', 'Dang', 'CSGO', 'Arma', ';)', 'Hi', 'Eight', 'Square', '100']
word1 = raw_input("Please input your fave word yo! ")
if word1 in array1:
	print "Sorry fam, we are broskis now m8."
else:
	array1.append(word1)
print array1

# THe Second Part of Assignment 5

name = raw_input("What is your name? ")
pets = raw_input("How many pets do you have? ")
color = raw_input("Favorite color? ")
array2 = [name, pets, color]
print (array2[0]+ "'s favorite color is " +array2[1]+ ". They have " + array2[2] + " pets.")