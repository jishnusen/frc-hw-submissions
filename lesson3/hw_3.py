if float(4.6) == 4.6:
	print "true"
#prints true

if int(4.6) == 4.6:
	print "true"
else:
	print "false"
#prints false

if int(4.6) == 4:
	print "true"
#prints true

print float("three point six")
#ValueError: could not convert string to float

print float("three")
#ValueError: could not convert string to float

print int("4 and 5")
#ValueError: invalid literal for int() with base 10


