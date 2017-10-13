class Robot:
	def __init__(self):
		self.arm = 0
		self.piece = False
		self.score = 0
		self.pos = 0
	def walk(self, dist):
		self.pos += dist
		print self.pos
	def armPos(self, height):
		self.arm += height
		print self.arm
	def pickCube(self):
		if self.pos == 3 and self.arm == 0 and self.piece == False:
			self.piece = True
			print "you have picked up a cube!"
		else:
			self.piece = False
			print "you cannot grab a cube."
	def scoreCube(self):
		if self.piece == True and self.arm == 10 and self.pos == 7:
			self.score += 1
			print "you have scored a point!"
		else:
			print "you cannot score a point."

my_robot = Robot()

my_robot.walk(3)
my_robot.armPos(0)

my_robot.pickCube()

my_robot.armPos(10)
my_robot.walk(4)

my_robot.scoreCube()