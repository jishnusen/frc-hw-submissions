array = []
inputs = ""


while inputs != "stop" and inputs != "Stop":
	inputs = raw_input("Input: ")

	if inputs != "stop" and inputs != "Stop":
		array.append(inputs)
print array