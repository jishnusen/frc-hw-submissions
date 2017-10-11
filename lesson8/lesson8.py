class Robot:
    def __init__(self):
        self.pos = 0
        self.armPos = 0
        self.score = 0
        self.hasCube = 0
    
    def move(self, num):
        self.pos += num
        print "Position of robot:",self.pos
    def raiseArm(self, num):
        self.armPos = self.armPos + num
        print "Arm position:",self.armPos

    def pickCube(self):
        if self.pos == 3:
            if self.armPos == 0:
                if self.hasCube == 0:
                    self.hasCube = 1
                    print "Robot picked up cube."
                else:
                    print "Robot has piece."
            else:
                print "Robot arm not in position."
        else:
            print "Robot not in position."
    def scoreCube(self):
        if self.pos == 7:
            if self.armPos == 10:
                if self.hasCube == 1:
                    self.score = self.score + 1
                    self.hasCube = 0
                    print "Robot scored. Score:",self.score
                else:
                    print "Robot doesn't have cube."
            else:
                print "Robot arm not in position."
        else:
            print "Robot not in position."


r = Robot()
while True:
    a = int(raw_input("How much do you want to move the arm: "))
    r.raiseArm(a)
    p = int(raw_input("How much do you want to move the robot: "))
    r.move(p)
    if raw_input("Pick up cube? ") == "yes":
        r.pickCube()
    if raw_input("Score cube? ") == "yes":
        r.scoreCube()
    if raw_input("Quit? ") == "yes":
        break
    
