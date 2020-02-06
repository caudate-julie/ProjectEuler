# What is the sum of the digits of the number 2^1000?

from time import time

def DigitSum(n):
    dsum = 0
    while n != 0:
        dsum += n%10
        n /= 10
    return dsum

ts = time()
print DigitSum(2**1000)
print "Time:", round(time() - ts, 4)
