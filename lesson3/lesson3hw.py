#Are float(4.6) and int(4.6) the same? If not, how are they different?
float(4.6)
int(4.6)
"""float equals the number within the parentheses. int rounds the decimal down to the whole number."""

#What does int(3.7) return?
int(3.7)
"""int(3.7) equals 3"""

#Does int(“4.5”) work? Does int(“4 and 5”)?
int("4.5")
int("4 and 5")
"""no, int("4.5") doesn't work. we can correct it by removing the quotation marks inside the parentheses. int("4 and 5") doesn't work either, you need to remove the quotation marks (which gives you 5)."""

#What happens when you try float(“three point six”)? Or float(“three”)?
float("three point six")
float("three")
"""float can work with quotations, but it can't work with words. you need to change the 'point' into '.', and 'three' into '3' """

#Check these one by one and comment out any lines that cause errors.
print "lesson 3 hw done. :)"