# if I use this program in many tasks,
# how can I switch it in without copying?
from time import time
from math import sqrt

primelist = [2, 3]
def NextPrime():
    if len(primelist) == 0:
        primelist.append(2) 
        return 2
    if len(primelist) == 1:
        primelist.append(3)
        return 3
    n = primelist[-1] + 2
    while True:
        t = sqrt(n)
        is_prime = True
        for x in primelist:
            if x > t:
                break
            if n % x == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(n)
            return n
        n += 2
    return

def Eratosthenes(MAX):
    bucket = range(MAX + 1)
    bucket[1] = 0
    for i in bucket:
        if i > 0:
            for not_prime in xrange(2 * i, MAX + 1, i):
                bucket[not_prime] = 0
    return bucket

timestart = time()
print Eratosthenes(1000000)
print "time: %.4f" % (time() - timestart)

def Cycles(a):
    if len(a) == 1:
        return [a]
    return list(x for y in (map(
        lambda(t):([a[i]]+t), Cycles(a[:i]+a[i+1:])
        ) for i in range(len(a))) for x in y)
