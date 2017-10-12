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
