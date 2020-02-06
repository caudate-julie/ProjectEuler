# Find the sum of all numbers which are equal
# to the sum of the factorial of their digits.

from time import time
from math import factorial

tn = 1
z = factorial(9)
while 10**tn < z*tn:
    tn += 1

NUM = 10**tn

def SetDigits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    return digits

def FacDeg(n):
    return n == sum(factorial(x) for x in SetDigits(n))

ts = time()
res = 0
for n in range(10, NUM):
    if FacDeg(n):
        print n
        res += n
print "Result:", res
print "Time:", round(time() - ts, 4)
