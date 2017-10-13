#Lesson 6 HW
#Part 1

user_array = []

user_choice = raw_input

print "Hi! Let's try having you add words to an array. Once you are done, just type stop."
print "Let's try it!"

while user_choice != "stop.":
	user_choice = raw_input("Give me an word.")

	if user_choice != "stop.":
		user_array.append(user_choice)

print user_array


#Part 2

my_array = ["good", "bad", "happy", "sad", "yes", "no", "hello", "bye", "hot", "cold"]
print my_array

arr2 = []
e = 9
for g in range(0,10):
	arr2.append(my_array[e])
	e -= 1
	g += 1
print arr2