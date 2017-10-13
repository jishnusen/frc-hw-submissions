
factors = []
def factor (x):
    for y in range(1, 10000000):
    if x % y == 0:
        factors.append(x)

factor (int(raw_input("Choose a number"))
print factors
        
        

