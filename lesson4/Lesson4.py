#Lesson 4: Conditionals and Booleans
age = int(raw_input("How many years old are you? "))
if age < 14:
	print "You can't do anything. Go play some more Mario Kart until you've reached puberty."
elif age >= 14 and age < 16:
	print "You can join the Citrus Circuits robotics team!"
elif age >= 16 and age < 18:
	print "You can join the Citrus Circuits robotics team!"
	print "You can now drive and get a job!"
elif age >= 18 and age < 21:
	print "You can join the Citrus Circuits robotics team!"
	print "You can now drive and get a job!"
	print "You're not yet an adult but you can go to college (not that I think you will)."
elif age >= 21 and age < 35:
	print "You can join the Citrus Circuits robotics team!"
	print "You can now drive and get a job!"
	print "You're not yet an adult but you can go to college (not that I think you will)."
	print "You're an adult now! Taxes! (yay)"
else age >=35:
	print "You can join the Citrus Circuits robotics team!"
	print "You can now drive and get a job!"
	print "You're not yet an adult but you can go to college (not that I think you will)."
	print "You're an adult now! Taxes! (yay)"
	print "You can become President now! (Again, not that you will.)"

#Lesson 4.5: The Software Engineering Process
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
  return weight / (height ** 2)
for patient in patients:
  weight, height = patients[0]
bmi = calculate_bmi(height, weight)
print "Patient's BMI is:" + str(bmi)

This program never defines patient in "for patient in patients"
