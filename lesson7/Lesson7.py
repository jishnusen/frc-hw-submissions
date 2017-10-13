def divisible(divide1, divide2):
    return divide1 % divide2 == 0
 
divide1 = int(raw_input("Give me a number  "))
divide2 = int(raw_input("Give me a different number "))

if divisible(divide1, divide2):
    print str(divide1) + " can be divided by " + str(divide2) 
else:
    print str(divide1) + " cant be divided by " + str(divide2)
