import Lesson9HomeworkClass as L

robot = L.Robot()
loop = True

print " "
print "Rules:"
print "1. The robot starts at position 0 with no cubes and the arm 0 inches off the ground."
print "2. A cube can only be picked up when:"
print "  a) The robot is at space 3 (3 meters from the starting position)."
print "  b) The arm is 0 inches off the ground."
print "  c) The robot does not already have a cube."
print "3. The robot must be holding a cube 10 inches off the ground at position 7 (7 meters from the starting position) to score."
print "4. Each time you score you get 5 points."
print " "

while loop == True:

	robot.move(int(raw_input("How many meters would you like to move? ")))
	robot.move_arm(int(raw_input("How many inches would you like to move the arm? ")))
	obtain_cube = raw_input("Would you like to try to pick up a cube? (y = Yes, n = No) ")
	if obtain_cube == "y":
		if robot.arm_position == 0 and robot.position == 3 and robot.cube == False:
			robot.cube = True
			print "You obtained a cube."
		else:
			print "You did not succesfully obtain a cube."
	score_attempt = raw_input("Would you like to attempt to score? (y = Yes, n = No) ")
	if score_attempt == "y":
		if robot.arm_position == 10 and robot.position == 7 and robot.cube == True:
			robot.score += 5
			print "Success!"
		else:
			print "You did not score."

	print " "
	print "Current position: " + str(robot.position) + " meters from start."
	print "Current arm position: " + str(robot.arm_position) + " inches from ground."
	print "Current score: " + str(robot.score) + " points."
	if robot.cube == True:
		print "You have a cube."
	else:
		print "You do not have a cube."
	print " "