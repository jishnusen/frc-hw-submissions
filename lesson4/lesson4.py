age = int(raw_input("How old are you? "))

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
