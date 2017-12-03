class robot:
	pos = 0
	armpos = 0
	piece = False
	score = 0

	def __init__(self, name, pos, armpos, piece, score):
		self.name = name
		self.pos = pos
		self.armpos = armpos
		self.piece = piece
		self.score = score

	def move(self, dist):
		if dist + self.pos <= 7 and dist + self.pos >= -7: 
			self.pos += dist
			return True
		else: 
			print "Invalid move."
			return False

	def arm(self, updown):
		self.armpos += updown

	def pickup(self):
		if self.pos == 3 and self.armpos == 0 and self.piece == False:
			self.piece = True
			print "You picked up a piece!"
			return True

	def win(self):
		if self.pos == 7 and self.armpos == 10 and self.piece == True:
			self.score = True
			print "You win!"

	def status(self):
		print "you are on space " + str(self.pos) + "."
		print "your arm is " + str(self.armpos) + " spaces high."
		if self.piece == True:
			print "you are holding a piece."
		else:
			print "you are not holding a piece."

	def choice(self):
		decision = False
		while decision == False:
			go = raw_input("do you want to move your robot or your arm? robot/arm ")
			if go == "robot":
				self.move(int(raw_input("how much do you want to move your robot?")))
				decision = True
			elif go == "arm":
				self.arm(int(raw_input("how much do you want to move your arm?")))
				decision = True

jishnu = robot("jishnu", 0, 0, False, False)

def play():
	while jishnu.score != True:
		jishnu.choice()
		jishnu.pickup()
		jishnu.status()
		jishnu.win()

play()




