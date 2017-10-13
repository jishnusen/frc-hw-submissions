

age = int(raw_input("Your age? "))

if age < 14:
	print "Sorry, you can't do anything... yet!"
elif age >= 14 and age < 16:
	print "You can join the awesome 1678 team! "
elif age >= 16 and age < 18:
	print "You can join the awesome 1678 team! "
	print "You can drive and get a job!"
elif age >=18 and age <21:
	print "You can join the awesome 1678 team! "
	print "You can drive and get a job!"
	print "You can attend college"
elif age >= 21 and age <35:
	print "You can join the awesome 1678 team! "
	print "You can drive and get a job! "
	print "You can attend college! "
	print "You are an adult! "
else:
	print "You can join the awesome 1678 team! "
	print "You can drive and get a job"
	print "You can attend college! "
	print "You are an adult! "
	print "You can become president! "
	
	
print ""
print ""
print ""

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
  return weight / (height ** 2)
for patient in patients:
  weight, height = patients[0]
#they switched height and weight
bmi = calculate_bmi(weight, height)
print "Patient's BMI is:" + str(bmi)
