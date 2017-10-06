a = raw_input("Rock, paper, or scissors?")
b = raw_input("Rock, paper, or scissors?")
if a == "Rock":
	if b == "Scissors":
		print "play 1 wins."
	elif b == "Paper":
		print "play 2 wins."
	else:
		print "Tie"
elif a == "Paper":
	if b == "Scissors":
		print "play 2 wins"
	elif b == "Rock":
		print "play 1 wins"
	else:
		print "Tie"
else:
	if b == "Scissors":
		print "Tie"
	elif b == "Paper":
		print "play 1 wins"
	else:
		print "Tie"