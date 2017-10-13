class robot():
    global clasp_on
    clasp_on = False
    global pos
    global armpos 
    armpos = 0
    def __init__(self, pos, armpos):
        self.pos = pos
        self.armpos = armpos
    def move(self, pos):
        while raw_input("press enter to move forward or stop to stop moving\n") != "stop":
            pos += 1
            print pos
            if pos == 3:
                clasp_on = bool(raw_input("If you want to grasp the cube type true\n"))
                if clasp_on == True:
                    print "good"
            elif pos == 7:
                print("You need to stop and lift the cube\n")

    def lift(self, armpos):
        while raw_input("press enter to lift up or stop to stop lifting\n") != "stop":
            score = 0
            armpos += 1
            print armpos
            if armpos == 10:
                score += 7
                print score
def running():
    robot_run = robot(0, 0)
    robot_run.move(0)
    robot_run.lift(0)

while raw_input("Should the robot run\n") != "no":
    running()












