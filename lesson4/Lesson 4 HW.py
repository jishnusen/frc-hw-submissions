age = int(raw_input("How old are you?"))
if age < 13:
	print "You are too young to join Citrus Circuits"
elif age >= 13 and age < 16:
	print "Congratulations, you can join Citrus Circuits"
elif age >= 16 and age < 18:
	print "Congratulations, you can drive. Don't die."
elif age >= 18 and age < 21:
	print "Congratulations, you can go to college and vote."
elif age >= 21 and age <35:
	print "Congratulations, you are an adult and can drink and stuff."
elif age >= 35 and age < 200:
	print "Congratulations, you can run for president and stuff."
else:
	print "Congratulations, you are immortal. All of your loved ones are probably dead. Happiness."
