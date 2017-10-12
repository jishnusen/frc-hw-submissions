array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
newArray = []
print "Original array: ", array
for i in range(len(array)):
    index = len(array) - i-1
    newArray.append(str(array[index]))
print "New array(reversed): ", newArray
