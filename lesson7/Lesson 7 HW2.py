
def Divide(a,b): 
 if a % b == 0:
   	print "These numbers are divisible."
 else:
   	print "These numbers are not divisible"

yay = int(raw_input("Choose a number: "))
woot = int(raw_input("Choose another number:"))

Divide(yay,woot)