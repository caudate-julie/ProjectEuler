# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n = 0.

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

def DichSearch(seq, n):
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


def PrimeNum(a, b):
    x = 0
    while True:
        y = x**2 + a*x + b
        if y < primes[-1]:
            if not DichSearch(primes, y):
                return x - 1
        elif y > primes[-1]:
            while y > primes[-1]:
                z = NextPrime(primes)
                primes.append(z)
            if y != z:
                return x-1
        x+=1

primes = [2]
mp = 0
j = 0
MAX_A = 1000
MAX_B = 1000
while True:
    while j > len(primes) - 1:
        primes.append(NextPrime(primes))
    if primes[j] > MAX_B:
        break
    b = primes[j]
    for a in range(-MAX_A+1, MAX_A):
        pn1 = PrimeNum(a, b)
        pn2 = PrimeNum(a, -b)
        if pn1 > mp:
            mp = pn1
            pair = (a, b)
        elif pn2 > mp:
            mp = pn2
            pair = (a, -b)
    j += 1
print "Result:", pair, mp
print "Answer:", pair[0]*pair[1]
ts = time()
print "Time:", round(time() - ts, 4)

