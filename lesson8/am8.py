class robot:
	global pos
	pos = 0
	global arm
	arm = 0
	global piece
	piece = False
	global score
	score = 0

	def mov(self, num):
		global space
		space += num
		print("Moved forward " + str(num) + ".")

	def arm(self, num):
		global arm
		arm += num
		print("Arm moved " + str(num) + ".")

	def pickup(self):
		global piece
		global pos
		global arm
		if piece == True or pos != 3 or arm != 0:
			print("Cannot pickup piece. ")
		else:
			piece = True
			print("Picked up piece.")

	def score(self):
		global piece
		global pos
		global arm
		if piece == False or pos != 7 or arm != 10:
			print("Cannot score.")
		else:
			print("Scored!")
			piece == False

	def automate():
		global pos
		global arm
		global piece
		global score
		mov(3-pos)
		arm(0-arm)
		pickup()
		mov(7-pos)
		arm(10-arm)
		score()


