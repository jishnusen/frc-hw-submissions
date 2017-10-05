name = raw_input("What is your name?")
x = int(raw_input("how many pizzas do you want?"))
y = int(raw_input("how many pieces of pepperoni?"))
z = int(raw_input("how many olives?"))
print name + " ordered " + str(x) + " pizzas with " + str(y) + " pepperonis and " + str(z) + " olives."

avg = (x + y + z) / 3

print "challenge: " + str(avg)