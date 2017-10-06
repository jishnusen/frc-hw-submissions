array = []

while input != "Stop":
	input = raw_input("Enter Something. ")
	array.append(input)

if input == "Stop":
	for i in range(0, len(array)-1):
		print array[i]

array = ["Laura", "Dog", "Grapes"]

reverse = []

for i in range(0, len(array)):
	reverse.append(array[len(array)- 1 - i])
	if (len(array) -1 -i) == 0:
		print reverse
		


