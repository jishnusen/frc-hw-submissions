class Middle_A:
	Hz = 440
	def __init__(self, player, Db):
		self.player = player
		self.Db = Db
print "Hello, conductor. Who'd you like to play the tuning note, and how loud?"
a = raw_input("What instrument")
b = float(raw_input("How loud (in Db)"))
MA1 = Middle_A(a, b)
print MA1.player, MA1.Db