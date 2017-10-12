array2 = []
name = raw_input("What is your name? ")
array2.append(name)
color = raw_input("What is your favorite color? ")
array2.append(color)
x = int(raw_input("How many pets do you have? "))
array2.append(x)
print array2[0] + "'s favorite color is", array2[1] + ". They have", array2[2], "pets."
