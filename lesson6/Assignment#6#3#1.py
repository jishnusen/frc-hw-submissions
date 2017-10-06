divisabilatyof3 = 3
divisabilatyof5 = 5

for i in range(100):
	isit3 = i / (divisabilatyof3 * 1.0)
	isit5 = i / (divisabilatyof5 * 1.0)

	if isit3 - (i / divisabilatyof3) == 0:
		print str(i) + " is divisible by 3"
	if isit5 - (i / divisabilatyof5) == 0:
		print str(i) + " is divisible by 5"