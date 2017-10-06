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