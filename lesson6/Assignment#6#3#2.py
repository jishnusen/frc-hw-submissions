numList = [1, 1]

for i in range(100):
	numList.append(numList[len(numList) - 1] + numList[len(numList) - 2])
	
	if (numList[len(numList) - 1] / 2.0) - (numList[len(numList) - 1] / 2) == 0:
		print numList[len(numList) - 1]