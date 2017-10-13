number = float(raw_input("Enter a number for its factors"))

factors = [1]
for x in range(1, 10000000):
    if number % x == 0:
        factors.append(x)
    
print (factors)
