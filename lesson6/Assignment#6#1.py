userWord = ""
newArray = ["ice", "fire", "cold"]
while userWord != "stop":
	userWord = raw_input("Type out a word(Make it school appropriate!)").lower()
	newArray.append(userWord)

print newArray