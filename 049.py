# What 12-digit number do you form by concatenating
# the three terms in this sequence?
# 

from math import sqrt
from time import time
from itertools import dropwhile

def primes():
    if len(primelist) == 0:
        primelist.append(2) 
        return
    if len(primelist) == 1:
        primelist.append(3)
        return
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
            return
        n += 2
    return

primelist = [2]
timestart = time()
while primelist[-1]<10000:
    primes()

def SameDigits(a, b):
    digs = []
    for x in (a, b):
        dig = []
        while x > 0:
            dig.append(x%10)
            x /= 10
        digs.append(dig)
    return sorted(digs[0]) == sorted(digs[1])


for x in dropwhile(lambda x: x < 1000, primelist):
    
print "Time: %.4f" % (time() - timestart)
