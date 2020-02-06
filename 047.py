# Find the first four consecutive integers to have
# four distinct primes factors.
# What is the first of these numbers?
# 1:51 - ...

from math import sqrt
from time import time
NUM = 4

def GetPrimeFactors(n):
    factors = []
    for x in primelist:
        if n%x == 0:
            factors.append(x)
            while n%x == 0:
                n /= x
        if n == 1:
            break
    while n>1:
        primes()
        x = primelist[-1]
        if n%x == 0:
            factors.append(x)
            while n%x == 0:
                n /= x
    return len(factors)

def primes():
    if len(primelist) == 0:
        primelist.append(2) 
        return 2
    if len(primelist) == 1:
        primelist.append(3)
        return 3
    n = primelist[-1] + 2
    while True:
        t = sqrt(n)
        flag = True
        for x in primelist:
            if x > t:
                break
            if n%x == 0:
                flag = False
                break
        if flag:
            primelist.append(n)
            return n
        n += 2

primelist = []
timestart = time()
n = 1
print "Go!"
while True:
    n += 1
    if n%1000 == 0:
        print n/1000, "curtime: %.4f" % (time() - timestart)
    flag = True
    for x in range(n, n+NUM):
        if GetPrimeFactors(x) != NUM:
            flag = False
            break
    if flag:
        break

print n
print "Time: %.4f" % (time() - timestart)
