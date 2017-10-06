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

