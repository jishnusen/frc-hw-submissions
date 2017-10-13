array = []
inputs = ""


while inputs != "stop" and inputs != "Stop":
	inputs = raw_input("Input: ")

	if inputs != "stop" and inputs != "Stop":
		array.append(inputs)
print array

print ""
print ""

variable = 5
array3 = []
while len(array3) < 5:
	array2 = [1, 2, 3, 4, 5]
	array3.append(variable)
	variable -= 1
print array3
