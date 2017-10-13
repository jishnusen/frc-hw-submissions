gender = raw_input("What is your gender?")
if gender =="female" or gender =="girl":
	gender = "miss."
elif gender == "male" or gender == "boy":
	gender = "sir."
age = int(raw_input("What is your age?"))
if age < 21:
	print "no hangovers tmrw morning lol"
	drink = raw_input("what non-alcoholic drink would u like bro")
else: 
	print "yee boi guess who's getting drunk tonight"
	drink = raw_input("what alcoholic drink would u like brah")
print "k bro, we'll order " + drink + "for you, " + gender
