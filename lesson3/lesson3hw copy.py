''' 
1. float(4.6) and int(4.6) are *not* the same
'''
if float(4.6) == int(4.6) 
	print "same"
else 
	print"not same"

''' 
2. int(3.7) returns 3.7 round down to 3
'''
print int(3.7)

'''
3. No, int("4.5") doesn't work because "4.5" is a string.
   int("4 and 5") doesn't work either.same reason
   there will be an error
'''


'''
4. Same as #3; float includes numbers (specifically decimals) not strings.
'''
