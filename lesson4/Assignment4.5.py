weight = [70, 80, 150]
height = [1.8, 1.9, 1.7]

def calculate_bmi(weight, height):
  return weight / height**2
for i in range (0, 3):
	bmi = calculate_bmi(weight[i], height[i])
	print "Patient's BMI is:" + str(bmi)