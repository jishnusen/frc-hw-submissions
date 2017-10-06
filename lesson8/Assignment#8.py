class Robot:

	def __init__(self, position, armPosition, piece):
		self.position = position
		self.armPosition = armPosition
		self.piece = piece
		self.points = 0

	def move(self, move):
		if self.position + move > 7:
			self.position = 7
		elif self.position + move <0:
			self.position = 0
		else:
			self.position += move

	def moveArm(self, moveArm):
		self.armPosition += moveArm

	def cube(self):
		self.piece = True

	def score(self):
		self.points += 5
		self.piece = False

	def printSelf(self):
		string = ""
		for i in range (0, 8):
			if i == self.position:
				string += " | "
			elif i == 3:
				string += ","
			else:
				string += "."
		print string

my_robot = Robot(0, 0, False)
my_robot.printSelf()

while my_robot.points < 10:
	print "Your score is " + str(my_robot.points) + " points"
	print "Your robot's arm is at " + str(my_robot.armPosition) + " units from the ground"
	my_robot.move(int(raw_input("How far do you want your robot to move? ")))
	my_robot.moveArm(int(raw_input("How far do yoou want your robot's arm to move? ")))
	my_robot.printSelf()
	if my_robot.piece == False:
		if my_robot.position == 3:
			my_robot.cube()
			print "You picked up the cube"
		else:
			print "the cube is " + str(3 - my_robot.position) + " units to your right"
	else:
		if my_robot.position == 7 and my_robot.armPosition == 10:
			my_robot.score()
			print "You scored!"
		elif my_robot.position == 7 and my_robot.armPosition != 10:
			print "Your arm needs to be 10 units from the ground for you to score."
		else:
			print "Your robot needs to be on the 7th block"

print "Congratulations you've Won!"

