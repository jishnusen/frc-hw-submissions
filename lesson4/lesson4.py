age = int(raw_input("How old are you?"))
one ="You can join robotics!"
two =" You can now drive and work."
three = " You can attend college."
four =" You are now an adult."
five =" Fun fact, you can now run for president, congratulations."
if age >= 14 and age < 16:
	print one
elif age >= 16 and age < 18:
	print one + two
elif age >= 18 and age < 21:
	print one + two + three
elif age >= 21 and age < 35:
	print one + two + three + four
elif age >= 35:
	print one + two + three + four + five
else:
	print "Sorry you dont meet requirements."