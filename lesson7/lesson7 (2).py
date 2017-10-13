def divisible(dividend, divisor):
    return dividend % divisor == 0
 
dividend = int(raw_input("Give me an integer: "))
divisor = int(raw_input("Give me another integer: "))

if divisible(dividend, divisor):
    print str(dividend) + " is divisible by " + str(divisor) + "!"
else:
    print str(dividend) + " is not divisible by " + str(divisor) + "!"
