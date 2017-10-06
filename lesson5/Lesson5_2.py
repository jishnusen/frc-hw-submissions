a1 = "one"
a2 = "two"
a3 = "three"
a4 = "five"
a5 = "four"
a6 = "six"
a7 = "seven"
a8 = "eight"
a9 = "nine"
a10 = "ten"
a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
b = False
for d in range(10):
	c = raw_input("Guess what words I'm hiding there are 10 of them. Type to guess!")
	if c in a:
		print "you got one! Try to get more!"
	else:
		b = True
	print "Unfortunatly, you lose."	
	print a
print "YOU WIN!!!!!!!"