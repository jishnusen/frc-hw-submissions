class Robot:
	starting_arm_pos = 0
	starting_robo_pos = 0
	starting_cube = False
	starting_score = 0

	def __init__(self, arm_pos, robo_pos, cube, score ):
		self.arm_pos = arm_pos
		self.robo_pos = robo_pos
		self.cube = cube
		self.score = score

	def move(self):
		a = int(raw_input("How far would you like to move?"))
		self.robo_pos += a
		if self.robo_pos < 0 or self.robo_pos > 7
			print "You drove off the map. You failed."
			self.score -= 5

	def armmove(self):
		b = int(raw_input("How far up do you want to move the arm?"))
		self.arm_pos += b
		if self.arm_pos < 0
			print "You can't move the arm down any farther."
		elif self.arm_pos > 7 
			print "You can't move the arm any higher"

	def pickblock(self):
		if self.robo_pos == 3 and self.cube = False and self.arm_pos = 0:
			self.cube = True
			print "You picked up a block"
		else:
			print "There is no block here"

    
    def scoreblock(self):
    	if self.robo_pos == 7 and self.armmove == 10 and self.cube == True:
    		print "You scored!"
    		self.score += 5
    		self.cube == False
    	else:
    		print "You didn't score"

print "You are trying to score 20 points. To score, you have to get  a cube in your claw and raise it up to height 10 when you are in space 7. Each block is worth 5 points. If you drive off, you lose 5 points. Good luck."
playerrobot = Robot(0, 0, False, 0)
while playerrobot.score < 20 and playerrobot.score > -20:
	c = raw_input("Move, Raise Arm, Pick Up Block, Score Block")
	if c == "Move":
		playerrobot.move()
	elif c == "Raise Arm":
		playerrobot.armmove()
	elif c == "Pick Up Block"
		playerrobot.pickupblock()
	elif c == "Score Block"
		playerrobot.scoreblock()
	else:
		print "That is not an action"
	print "Score: ", playerrobot.score
	print "Current position: ", playerrobot.robo_pos
	print "Current arm height: ", playerrobot.arm_pos
print "You win. Congratulations."
