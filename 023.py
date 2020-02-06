# Find the sum of all the positive integers
# which cannot be written as the sum of two abundant numbers.

from time import time
from math import sqrt

def NextPrime (primelist):
    if len(primelist) == 0:
        return 2
    if len(primelist) == 1:
        return 3
    n = primelist[-1] + 2
    t = sqrt(n)
    while True:
        flag = True
        for x in primelist:
            if x > t:
                break
            if n%x == 0:
                flag = False
                break
        if flag:
            return n
        n += 2

def FactorDeg(n, x):
    xdeg = 0
    while n%x == 0:
        xdeg += 1
        n /= x
    return (n, xdeg)

def FactorSet(pfactors):
    if len(pfactors) == 0:
        return [1]
    x, xdeg = pfactors[0]
    getset = FactorSet(pfactors[1:])
    newset = []
    for i in range(xdeg + 1):
        y = x**i
        for z in getset:
            newset.append(y*z)
    return newset

def GetFactors(n):
    primefactors = []
    for x in primes:
        if n == 1:
            break
        if n%x == 0:
            n, xdeg = FactorDeg(n, x)
            primefactors.append((x, xdeg))
    while n > 1:
        x = NextPrime(primes)
        primes.append(x)
        if n%x == 0:
            n, xdeg = FactorDeg(n, x)
            primefactors.append((x, xdeg))
    return sorted(FactorSet(primefactors))[:-1]

def Search(seq, n):
    a = 0
    c = len(seq)
    while True:
        if c - a == 1:
            return seq[a] == n
        if a == c:
            return False
        b = (a+c)/2
        if seq[b] == n:
            return True
        elif seq[b] > n:
            c = b
        else:
            a = b        

def TaskSolve(MAX):
    abundant = []
    result = 0
    count = 0
    for n in range(1, MAX):
        if n < sum(GetFactors(n)):
            abundant.append(n)
    print "Sequence done!", len(abundant)
    itertime = time()
    for x in range(1, MAX):
        count += 1
        if count%1000 == 0:
            print count, round(time()-itertime, 4)
            itertime = time()
        flag = True
        for a in abundant:
            if a > x/2:
                break
            if Search(abundant, x-a):
                flag = False
                break
        if flag:
            result += x
    print
    print
    return result

primes = []
MAX = 28124
ts = time()
print TaskSolve(MAX)
print "Time:", round(time() - ts, 4)
