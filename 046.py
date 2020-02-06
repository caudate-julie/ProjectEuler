# What is the smallest odd composite that cannot be
# written as the sum of a prime and twice a square?
# 00:47 - 01:47

from math import sqrt
from time import time

def primes(m):
    primelist = []
    if len(primelist) == 0:
        primelist.append(2) 
        yield 2
    if len(primelist) == 1:
        primelist.append(3)
        yield 3
    n = primelist[-1] + 2
    while n < m:
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
            yield n
        n += 2
    return

timestart = time()
print 'Go!'
flag = True
d1 = 3
while flag:
    if d1%101 == 0:
        print "%d, curtime: %.4f" % (d1, time() - timestart)
    for d2 in range(3, d1+1, 2):
        n = d1 * d2
        flag = False
        for x in primes(n):
            if sqrt((n - x)/2) == int(sqrt((n - x)/2)):
                flag = True
                break
        if not flag:
            break
    d1 += 2

print "Result:\n", n
print "Time: %.4f" % (time() - timestart)
