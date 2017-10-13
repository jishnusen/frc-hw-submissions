class Robot:
	position = 0
	arm_position = 0 
	piece = False
	scorePoint = 0
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
	def walk(self, dist):
		self.pos += dist
	def armPosition(self, height):
		self.height = height
	def pickCube(self):
		if pos == 3 and height == 0 and piece == False:
			piece = True
			print "You have picked up a cube!"
		else: 
			piece = False
			print "You can't grab a cube."
	def scoreCube(self, point):
		self.point = point
		if piece == True and height == 10 and pos == 7:
			scorePoint == 1
			print "You have scored one point!"
		else:
			print "You can't score a point"
my_robot = Robot("michael", 0)
my_robot.walk(3)
my_robot.armPosition(0)
my_robot.pickCube()
my_robot.height(10)
my_robot.walk(4)
my_robot.scoreCube(1)

