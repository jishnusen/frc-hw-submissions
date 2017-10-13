my_squad = ["annie", "manulya", "nick", "alex", "siddarth", "lena", "nathan", "mohamed", "marley", "lauren"]
new = raw_input("who do you want to join my squad?")

if new in my_squad:
	print new + " is in my squad already."
else: 
	print new + " can join my squad."
	my_squad.append(new)
print my_squad