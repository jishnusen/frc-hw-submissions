print "1."
print "Type 'stop' when you want to stop adding to the array."
array = []
a = ""
while a != "stop":
	a = raw_input("What would you like to add to the array? ")
	array.append(a)
for i in range(0, len(array) - 1):
	print array[i]

print ""
print "2."
array2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "and", "z"]
print array2
print " "
print array2[::-1]

print ""
print "3. Extra Challenge"
print " "
print "1."
sum1 = 0
for j in range(1000):
	if j % 3 == 0 or j % 5 == 0:
		sum1 += j
print sum1

print ""
print "2."
sum2 = 0
for k in range(4000000):
	if k % 2 == 0:
		sum2 += k
print sum2

print ""
print "3."

import math
factors = []
allPrime = False
def divisible(a,b):
	return a % b == 0

def isPrime(num):
	prime = True
	for i in range(2,num):
		if divisible(num,i):
			prime = False
	return prime

def findFactors(num):
	for i in range(2,int(math.sqrt(num))):
		if divisible(num,i):
			if isPrime(i):
				factors.append(i)

findFactors(600851475143)
print factors