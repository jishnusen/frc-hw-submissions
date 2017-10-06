array = ["Ice", "Fire", "Earth", "Air"]
rev_array = []

for i in range(1, len(array) + 1):
	rev_array.append(array[(i * -1)])

print rev_array