class Robot:
    def __init__(self, position=0, arm_position=0, has_cube=False):
        self.position = position
        self.arm_position = arm_position
        self.has_cube = has_cube
        self.score = 0
        
    def move(self, amount_to_move):
        futurepos = self.position + amount_to_move
        if futurepos > 7 or futurepos < 0:
            raise RobotException('TOO FAR, FELL OFF TABLE')
            #print "TOO FAR, FELL OFF TABLE"
            #return
        self.position += amount_to_move
        
    def move_arm(self, amount_to_move):
        if self.arm_position + amount_to_move > 10:
            print "Cannot move arm any higher"
            return
        elif self.arm_position + amount_to_move < 0:
            print "Cannot move arm lower"
            return 
        self.arm_position += amount_to_move
        
    def pickupcube(self):
        if self.has_cube:
            print "Robot already has cube!!! :'("
        
        if self.arm_position!=0:
            print "fix yo arm position"
        
        if self.position !=3:
            print "fix yo position THEN come talk to me!"
        
        if (not self.has_cube) and self.position == 3 and self.arm_position == 0:
            self.has_cube = True

    def do_score(self):
        if self.has_cube and self.position == 7 and self.arm_position == 10:
            self.score += 1
            self.has_cube = False
            print "You FINALLY scored a point... :3 "
        else:
            print "Uh...no...nice try"

#position = int(raw_input("Position: ")
reggie = Robot(3, 4, True)
while reggie.score < 3:
    todo=raw_input("What do you want to do: (Move Robot, Move Arm, Pick up Cube, Score) ").lower().strip()
    if todo == "move robot":
        try:
            move= int(raw_input("How much do you want to move? ").strip())
            reggie.move(move)
        except ValueError:
            print 'NO NOT A NUMBERZZ!!'
    elif todo == "move arm":
        try:
            armmove = int(raw_input("How much do you want to move the arm? ").strip())
            reggie.move_arm(armmove)
        except ValueError:
            print 'NO NOT A NUMBER!!'
    elif todo == "pick up cube":
        reggie.pickupcube()
    elif todo == "score":
        reggie.do_score()
    else:
        print "You thought you could get away with not typing the right thing... NOPE!!! TRY AGAIN!"
        