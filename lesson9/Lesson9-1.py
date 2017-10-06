import DYRBotclass
print "Your goal is to score 20 points. To do that, you must go to position 3, pick up a block, go to position seven, get it up to height 10, and finally score the block. Each block is worth 5 points, so you must do that 4 times too win. BTW your crane is very unstable, so any mistake will result in loss of 5 points. Good luck."
playerrobot = DYRBotclass.DYRBot(0, 0, False, 0)
while playerrobot.score < 20:
	c = raw_input("Move, Raise Arm, Pick Up Block, Score Block.")
	if c == "Move":
		playerrobot.move()
	elif c == "Raise Arm":
		playerrobot.armmove()
	elif c == "Pick Up Block":
		playerrobot.pickupblock()
	elif c == "Score Block":
		playerrobot.scoreblock()
	else:
		print "You messed up. That's not an action. You lose!"
		playerrobot.score -= 5
	print "Score:", playerrobot.score
	print "Current position:", playerrobot.position
	print "Current arm height:",playerrobot.armheight
print "You win. You did it. Congratulations!!"