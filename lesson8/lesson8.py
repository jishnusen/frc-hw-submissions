class Robot:
	def __init__(self, position, armPosition, hasPiece, score):
		self.position = 0
		self.armPosition = 0
		self.hasPiece = 0
		self.score = 0

	def move(self, num):
		self.position += num
		print self.position

	def raiseArm(self, num):
		self.armPosition += num
		print self.armPosition

	def pickCube(self):
		if self.position == 3:
			if self.armPosition == 0:
				if self.hasPiece == 0:
					self.hasPiece += 1
					print "You picked up a cube"
	def scoreCube(self):
		if self.position == 7:
			if self.armPosition == 10:
				if self.hasPiece == 1:
					self.score += 1
					print "You Scored!!!!"

r = Robot(0,0,0,0)
r.move(3)
r.pickCube()
r.move(4)
r.raiseArm(10)
r.scoreCube()

