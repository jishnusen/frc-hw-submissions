print float(4.6)
print int(4.6)

#Float prints decimals while integer only prints the number cut off to the whole number

print int(3.7)

#It will print 3 because it's an integer type so it cuts off the value at the whole number

print int("4.5")

#No because it mixes string types with number types

print int("4 and 5")

#Without the int() it would work because it would just print "4 and 5" but because there's int() in front of it, it'll cause an error as it mixes string types with integer types

print float("three point six")

#No... this won't work either because it's a string type in an number types.

print float("three")

#Same as the problem before, it mixes number types with string types.