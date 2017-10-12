a = raw_input("meh.")
b = raw_input("mez")
c = raw_input("bhjbkhbfdjhg")
success = False
while (success == False):
	e = int(round(float(raw_input("number from 1-3."))))-1
	if e>=0 and e<=2:
		success = True

d = [a, b, c]
print d[e]