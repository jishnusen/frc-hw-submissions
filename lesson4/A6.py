age = int(raw_input("How old are you? "))

if age >= 14 and age < 16:
	print "You can join the robotics team" 
elif age >= 16 and age < 18:
	print "You can join the robotics team, and get a drivers lisence"
elif age >=18 and age < 21:
	print "You can join the robotics team, get a lisence, and go to college"
elif age >= 21 and age < 35:
	print "You can join the robotics team, get a lisence." 
	print "You can go to college, and you are an adult"
elif age >= 35:
	print "You can join the robotics team, get a lisence."
	print "You can go to college, you are an adult."
	print "and become president."
elif age < 14 and age >= 0:
	print "You are too young to do anything"
else:
	print "You did not follow directions"






