a = float(raw_input("How old are you?"))
if a < 13:
	b = raw_input("What grade are you in?")
	if b == "8th":
		print "You can join Citrus Circuits!!!!!!!!!1!!!!"
	else:
		print "Bye, uneducated one."
elif a >= 14 and a < 16:
	print "You can join CC!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!"
elif a >= 16 and a < 18:
	print "Driving and CC for you."
elif a >= 18 and a < 21:
	print "College + driving for you. Yay."
elif a > 1000:
	print "Congratulations, you are immortal. All your loved ones will die. Poor you."
	c = int(raw_input("How many limbs do you have left?"))
	if c == 4:
		print "Wow, you have taken good care of yourself."
	elif c >= 1 and c <= 3:
		print "Pretty typical. Keep holding on to those lucky limbs."
	elif c == 0:
		print "Yup, you potato. Immortal potato."
	else:
		print "Wat?"
else:
	print "OLD!!!!! All of the things (Except CC)"