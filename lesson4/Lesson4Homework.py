print "Lesson 4"
age = int(raw_input("Age, please! "))
if age<0:
	print "Um... no... Just... no..."
if age<5 and age>0:
	print "Wow... littluns get computers mighty early, don't they?"
	print "Back in my day..."
if age<14 and age>4:
	print "GO AWAY CHILD! YOU HAVE NO RIGHTS!"
if age>=14 and age<=18:
	print "So... you can join robotics now, which is cool! Psst... Join progamming, why donchya?"
if age>=16:
	print "You can start driving, which is cool. I don't even have my permit yet. :("
if age>=18:
	print "You're an adult! Is that a good thing?"
if age>=21:
	print "You can drink now! If you really want to? I guess..."
if age>=35:
	print "You can be President now! Not that you WILL be, but you CAN be!"
if age>100:
	print "Um... no. Is it terrible to say I don't believe you? But hey, if it's true, I'm sorry, I mean no disrespect."
if age>110:
	print "Nope."

print " "
print "Lesson 4.5"
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
	return weight / (height ** 2)
for patient in patients:
	weight, height = patient
	bmi = calculate_bmi(weight, height)
	print "Patient's BMI is: " + str(bmi)