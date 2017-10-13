country_array = ["georgia", "laos", "cambodia", "jordan", "burundi", "paraguay", "slovenia", "honduras", "albania", "kazakhstan"]

last_index = len(country_array)-1
array = []

for i in range(last_index, -1, -1): 
    array.append(country_array[i])

print array
