class Robot:

	def __init__(self, pos, arm, grab, score):
		self.pos = pos
		self.arm = arm
		self.grab = grab
		self.score = score

	def move(self, pos):
		while raw_input("do you want to move the robot?") != "no":
			pos += 1
			print "your position is " + str(pos) + "."
	def lift(self, arm):
		while raw_input("do you want to lift the arm?") != "no":
			arm += 1
			print "your arm is " + str(arm) + " high."
	def claw(self, grab, pos, arm):
		if raw_input("do you want to close the claw?") != "yes":
			grab = 2
			print "the claw is open"
		else:
			print "the claw is closed"
			if pos == 3 and arm == 0:
				grab = 0
				print "you have grabbed a block!"
			else:
				print "you have not grabbed a block :("

	def points(self, score):
		if grab == 0:
			if raw_input("do you want to try and score?") != "no":
				print "you moved forwards " + (pos+(7-pos)) 
				print ". you lifted your arm " + (arm + (10-arm)) + "."
				pos= (7) 
				arm= (10) 
				grab = 2 
				score += 1
				print "your score is " + score
				print "your claw is now open"
			else: 
				print "ok"
		else:
			print "your score is " + score



my_robot = Robot(0, 0, 0, 0)
my_robot.move(0)
my_robot.lift(0)
my_robot.claw(0, 0, 0)
my_robot.points(0)
	




	