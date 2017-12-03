import lesson8

jishnu = lesson8.robot("jishnu", 0, 0, False, False)

def play():
	while jishnu.score != True:
		jishnu.choice()
		jishnu.pickup()
		jishnu.status()
		jishnu.win()

play()