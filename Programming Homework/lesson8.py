class Robot:
	starting_arm_pos = 0
	starting_cube = False
	starting_rob_pos = 0
	starting_score = 0
	def ____init____(self, starting_cube, starting_rob_pos, starting_arm_pos, starting_score):
		self.name = name
		self.pos = pos
		self.starting_rob_pos = robot
		self.starting_cube = cube
		self.starting_arm_pos = arm
		self.starting_score = score
	def walk(self,dist):
		self.pos+= dist
my_robot = Robot("robot", 0)
my_robot.walk(5)	
print my_robot.pos
