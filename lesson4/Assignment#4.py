age = int(raw_input("What's your age?\n"))

if age >= 14:
	print "You can join robotics"
	if age >= 16:
		print "You can drive/work"
		if age >= 18:
			print "You can go to college"
			if age >= 21:
				print "You can drink/smoke"
				if age >= 35:
					print "You can become President"
else:
	print "Your too young"