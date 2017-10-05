print "Welcome to the bar,"
a = int(raw_input("What's your age?"))
if a > 21:
	print "Come in."
elif a == 21:
	b = raw_input("This your first time?")
	if b == "Yes":
		print "Have fun."
	elif b == "No":
		print "Ok ... then??"
	else:
		print "That's a nonsense answer. Come in."
else:
	print "Get out."	