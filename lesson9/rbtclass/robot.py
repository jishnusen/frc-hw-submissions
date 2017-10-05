global pos
pos = 0
global arm
armp = 0
global piece
piece = False
global score
score = 0

def mov(num):
	global pos
	pos += num
	print("Moved forward " + str(num) + ".")

def arm(num):
	global armp
	armp += num
	print("Arm moved " + str(num) + ".")

def pickup():
	global piece
	global pos
	global armp
	if piece == True or pos != 3 or armp != 0:
		print("Cannot pickup piece. ")
	else:
		piece = True
		print("Picked up piece.")

def score():
	global piece
	global pos
	global armp
	if piece == False or pos != 7 or armp != 10:
		print("Cannot score.")
	else:
		print("Scored!")
		piece == False

def automate():
	global pos
	global armp
	global piece
	global score
	mov(3-pos)
	arm(0-armp)
	pickup()
	mov(7-pos)
	arm(10-armp)
	score()