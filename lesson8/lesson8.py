class Robot:
	startposition = 0
	startarm = 0
	startpiece = False
	startscore = 0

	def __init__(self, position, arm, piece, score):
		self.position = position
		self.arm = arm
		self.piece = piece
		self.score = score


	def positionRobot(self, dist):
		self.position += dist

	def armRobot(self, height):
		self.arm += height

	def pieceRobot(self, ok):
		self.piece = True

	def scoreRobot(self, cheese):
		self.score += cheese


def distance(a):
	valueOne = False
	moveOne = raw_input("Do you want to move?\n")
	if moveOne == "1":
		moveOne_distance = raw_input("How far?\n")
	print "Answer with 1-7"
	if a == "1":
		self.positionRobot(1)
		valueOne = True
	elif a == "2":
		self.positionRobot(2)
		valueOne = True
	elif a == "3":
		self.positionRobot(3)
		valueOne = True
	elif a == "4":
		self.positionRobot(4)
		valueOne = True
	elif a == "5":
		self.positionRobot(5)
		valueOne = True
	elif a == "6":
		self.positionRobot(6)
		valueOne = True
	elif a == "7":
		self.positionRobot(7)
		valueOne = True
	else:
		print "Try to actually enter something this time."
print "Use '1' to say yes, and '2' to say no."
distance(a)
armOne = raw_input("Do you want to move your arm height?\n")
if armOne == "1":
	armOne_height = raw_input("How tall")
if moveOne == "3": 
	print "You've picked up a piece!"
	piece = True
if position == 7 and piece == True and arm == 10:
	print "Congrats! You've won!"
	score += 5
	print score
if moveOne > 7:
	print "Input something lower than 8 please!"