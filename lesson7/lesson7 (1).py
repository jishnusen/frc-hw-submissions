def print_user_info(name, age):
    print name
    print age
    print age * 12

def pizza_shop(name, pizza, pepperoni, olives):
    print name, " ordered ", pizza, " pizzas with ", pepperoni, "pepperoni and ", olives, " olives!"

def age_conditions(age):
    if age < 14:
        print "You're young"
    elif age < 16:
        print "You can join the robotics team!"
    elif age < 18:
        print "You can drive."
    elif age < 21:
        print "You can go to college!"
    elif age < 35:
        print "You are an adult!"
    else:
        print "You can be president!"


def word_in_array(array, word):
    if word in array:
        print "You word exists in the array!"
    else:
        array.append(word)
        print "Your word was added to the array!"

    print array

def user_info(name, color, num_pets):
    user_info = []
    user_info.append(name)
    user_info.append(color)
    user_info.append(num_pets)
    print user_info[0] + "'s favorite color is " + user_info[1] + ". They have " + user_info[2] + " pets."

def add_to_array(array):
    user_input = ""
    
    while user_input != "stop":
        user_input = raw_input("Give me a word: ")
        if user_input != "stop":
            array.append(user_input)
      
    print array

def reverse_array(array):
    last_index = len(country_array)-1
    reverse_array = []

    for i in range(last_index, -1, -1):
        reverse_array.append(country_array[i])

    print reverse_array
