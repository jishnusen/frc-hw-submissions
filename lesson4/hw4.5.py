#Lesson 4.5 HW

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
    return weight / (height ** 2)
for patient in patients:
   	weight, height = patients[0]
   	bmi = calculate_bmi(height, weight)
print "Patient's BMI is:" + str(bmi)