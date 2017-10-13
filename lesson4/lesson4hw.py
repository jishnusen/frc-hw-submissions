
age = int(raw_input("How old are you?" ))

if age < 14:
	print "YOU MAY *NOT* JOIN THE ROBOTICS TEAM!! GO AWAY!! try again when you're 14..."
else:
	print "You *MAY* join the team!! Congrats!"



#---------------------------------------------------------------------------------------------------


drive = int(raw_input("How old are you?" ))

if age < 16:
	print "YOU MAY *NOT* DRIVE OR GET A JOB!! GO AWAY!! try again when you're 16..."
else:
	print "You *MAY* drive and get a job!! Congrats!"



#---------------------------------------------------------------------------------------------------


college = int(raw_input("How old are you?" ))

if age < 18:
	print "YOU MAY *NOT* ATTEND COLLEGE!! GO AWAY!! try again when you're 18..."
else:
	print "You *MAY* attend college!! Congrats!"



#---------------------------------------------------------------------------------------------------


adult = int(raw_input("How old are you?" ))

if adult < 21:
	print "YOU ARE *NOT* AN ADULT!! GO AWAY!! try again when you're 21..."
else:
	print "You *ARE* AN ADULT!! Congrats!"


#---------------------------------------------------------------------------------------------------

prez = int(raw_input("How old are you?" ))

if prez < 35:
	print "YOU MAY *NOT* BE A PREZ!! GO AWAY!! try again when you're 35..."
else:
	print "You *MAY* BE AN PREZ!! Congrats!"

#---------------------------------------------------------------------------------------------------


patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
  return weight / (height ** 2)
for patient in patients:
  weight, height = patients[0]
bmi = calculate_bmi(weight, height)
print "Patient's BMI is:" + str(bmi)

