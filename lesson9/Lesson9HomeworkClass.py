class Robot:
	position = 0
	arm_position = 0
	cube = False
	score = 0

	def move(self, dist):
		self.position += dist

	def move_arm(self, arm):
		self.arm_position += arm