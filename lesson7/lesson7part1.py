def lesson1(name,age):
    print "Your name is " + name
    monthAge = age * 12
    print "You are " + str(age) + " years old"
    print "Your age in months is " + str(monthAge)

def lesson2(name,x,y,z):
    print "We will order",str(x),"pizzas,",str(y),"pepperonis and",str(z),"olives for", name

def lesson2challenge(firstInt,secondInt,thirdInt):
    averageInt = (firstInt + secondInt + thirdInt)/3
    print "The average of your three numbers is", averageInt

def lesson4(age):
    if age>=35:
        print "You can become president."
    if age>=21:
        print "You are an adult."
    if age>=18:
        print "You can attend college."
    if age>=16:
        print "You can drive and get a job."
    if age>=14:
        print "You can join the robotics team."
    if age<14:
        print "You can't do anything."

def lesson5part1(userInput):
    array = ["joe","jack","one","out","name","alex","word","something","the","people"]
    isWord = False
    for word in array:
        if userInput == word:
            print "That's a word in the list!"
            isWord = True
            break
    if isWord == False:
        array.append(userInput)
    print array

def lesson5part2(name,color,x):
    array2 = []
    array2.append(name)
    array2.append(color)
    array2.append(x)
    print array2[0] + "'s favorite color is", array2[1] + ". They have", array2[2], "pets."

def lesson6part1():
    x = 1
    array = []
    while x == 1:
            userInput = raw_input("Enter a word: ")
            if userInput == "stop":
                    x = 10
                    print array
            else:
                    array.append(userInput)

def lesson6part2():
    array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    newArray = []
    print "Original array: ", array
    for i in range(len(array)):
        index = len(array) - i-1
        newArray.append(str(array[index]))
    print "New array(reversed): ", newArray

def lesson6part3():
    #Problem 1
    numSum = 0
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
            numSum += i
    print "Sum of factors of 3 or 5 under 1000:",numSum
            
    #Problem 2
    #Fibonacci sequence starts as 1,2,3,5,8 in this program
    #Because the problem states that it starts as 1,2,3,5,8
    fibnum1 = 0
    fibnum2 = 1
    nextnum = 0
    evensum = 0
    while True:
        nextnum = fibnum1 + fibnum2
        fibnum1 = fibnum2
        fibnum2 = nextnum
        if nextnum >= 4000000: #four million
            break
        if nextnum%2 == 0:
            evensum += nextnum
    print "Sum of even numbers inf Fibonacci seq:",evensum

    #Problem 3
    def is_prime(a):
        i = 2
        while a%i !=0:
            i+=1
        if a == i:
            return True
        else:
            return False

    largnum = 600851475143
    numsqrt = largnum**(0.5)
    ind = -1
    d = 2
    factors = []
    while True:
        if largnum % d == 0:
            if is_prime(d) == True:
                factors.append(d)
                ind += 1
        if float(d) >= numsqrt:
            break
        d+=1

    print "Largest prime factor:",factors[ind]
