things = []

needs = raw_input("What do you need?")

while needs != "stop":
	needs = raw_input("What do you need?")	
	things.append(needs)

if needs == "stop":
	print things



