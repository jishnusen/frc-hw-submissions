class Robot:
	position = 0
	armposition = 0
	piece = "No"
	score = 0
	def movePos(self, a):
		self.position += a
	def moveArm(self, a):
		self.armposition = self.armposition + a
	def pickup():
		if position == 3:
			print "You are in position to pick up a piece."
		elif armposition == 0 and position == 0:
			print "You have picked up a piece."
		elif position != 3:
			print "You are not in position to pick up a piece."
		elif armposition != 0:
			print "Lower you arm to position 0."
	def scored():
		if position == 7 and armposition == 10:
			score = score + 5
			print "You have scored, your score is now" + score
		elif position != 7:
			print "You arent in position to score."
		elif armposition != 10:
			print "Your arm is not in position to score, raise by ten inches."





my_robot = Robot()


movement = int(raw_input("How many m would you like your robot to move.( Negative to move to the left)"))
arm = int(raw_input("How high would you like your arm to be.(Negative to go down)"))
my_robot.movePos(movement)
my_robot.moveArm(arm)
print "Your robot is at ", + my_robot.position + ," and his arm is at", + my_robot.armposition
if movement == 3 and arm == 0:
	print "You have picked up a piece."
elif movement == 7 and arm == 10:
	print " You have scored."
         