#The sequence of triangle numbers is generated by adding the natural
#numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 
#+ 7 = 28. The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#
#We can see that 28 is the first triangle number to have over five\
#divisors.
#
#What is the value of the first triangle number to have over five
#hundred divisors?

import sys
sys.path.append('../utils')
from utils import d

def p12(num_divisors):
    i = 1
    cnt = 0
    while cnt <= num_divisors:
        if i % 2 == 0:
            cnt = d(i / 2) * d(i + 1)
        else:
            cnt = d(i) * d((i + 1) / 2)
        i += 1
    return i

m = p12(500)
print m * (m - 1) / 2
