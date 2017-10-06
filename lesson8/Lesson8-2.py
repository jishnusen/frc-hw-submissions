class DYRBot:
	color = "#a03494"
	startpos = 0
	startpiece = False
	startscore = 0

	def __init__(self, position, armheight, piece, score):
		self.position = position
		self.armheight = armheight
		self.piece = piece
		self.score = score
		
	def move(self):
		a = int(raw_input("How much do you want to move by?"))
		self.position += a
		if self.position < 0 or self.position > 7:
			print "You drove off the map. You failed!"
			self.score -= 5
	def armmove(self):
		b = int(raw_input("How much do you want to move the arm vertical by?"))
		self.armheight += b
		if self.armheight < 0 or self.armheight > 10:
			print "You pushed the crane too far. You failed!"
			self.score -= 5

	def pickupblock(self):
		if self.position == 3 and self.piece == False:
			self.piece = True
			print "You picked up a block"
		else:
			print "You activated piece picup wth no piece at your location, you lose."
			self.score -= 5
	def scoreblock(self):
		if self.position == 7 and self.armheight == 10 and self.piece == True:
			print "Good job, you scored"
			self.score += 5
			self.piece = False
		else:
			print "You messed up."
			self.score -= 5
print "Your goal is to score 20 points. To do that, you must go to position 3, pick up a block, go to position seven, get it up to height 10, and finally score the block. Each block is worth 5 points, so you must do that 4 times too win. BTW your crane is very unstable, so any mistake will result in loss of 5 points. Good luck."
playerrobot = DYRBot(0, 0, False, 0)
while playerrobot.score < 20 and playerrobot.score > -20:
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