# Which prime, below one-million, can be written
# as the sum of the most consecutive primes?
# 20:09 - 20:44

from time import time
from math import sqrt
from bisect import bisect_left

MAX = 1000000

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

timestart = timediff = time()
primelist = [2]
while primelist[-1] < MAX:
    primes()
maxlen = 1
m = len(primelist) - 1
flag = False
print m
for k in reversed(range(1, m)):
    if k%100 == 0:
        print "Len: %d, time: %.2f, difference: %.3f" % (k, time() - timestart, time() - timediff)
        timediff = time()
    for j in range(m-k):
        p = sum(primelist[j:j+k])
        if p > MAX:
            break
        if primelist[bisect_left(primelist, p)] == p:
            print k
            flag = True
            break
    if flag:
        break

print "Result:\n", p
print "Time: %.4f" % (time() - timestart)
