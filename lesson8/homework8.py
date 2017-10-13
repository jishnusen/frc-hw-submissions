class Robot():
	position = 0
	armPos = 5
	hasCube = False
	score = 0

	def __init__(self):
		pass
	def raiseLower(self, pos):	#Raises and lowers the arm.
		self.armPos = pos
		print "Your arm is at position " +str(self.armPos)+ "."
	def move(self, pos):
		self.position += pos
		print "You are now " + str(self.position)+ " meters from start."
	def pickUp(self):
		if [self.armPos == 0 and self.hasCube == 0 and self.position == 3]:
			self.hasCube = True
		elif self.hasCube == True:
			print "You already have a cube!"
		else:
			print "You must be 3 meters away from start and have your arm at posistion 0 to pick up a cube."
	def scorePoint(self):
		if self.hasCube == True and self.armPos == 10 and self.position == 7:
			self.score += 5
		elif self.hasCube == False:
			print "You need a cube to score!"
		elif self.armPos != 10:
			print "Your arm needs to be at position 10!"
			print "Right now your arm is at position "+str(self.armPos)+ "."
		elif self.position != 7:
			print "You need to be at position 7 to score cubes!"
			print "Right now you are at position " + str(self.position) +"."

robot = Robot()
robot.raiseLower(10)
