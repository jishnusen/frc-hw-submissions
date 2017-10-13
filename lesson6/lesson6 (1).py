input_array = []
user_input = ""

while user_input != "stop":
    user_input = raw_input("Give me a word: ")
    if user_input != "stop":
       input_array.append(user_input)

print input_array
