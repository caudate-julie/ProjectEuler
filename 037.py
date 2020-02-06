# Find the sum of the only eleven primes that are both
# truncatable from left to right and right to left.

from time import time
from math import sqrt

NUM = 11

def NextPrime (primelist):
    if len(primelist) == 0:
        return 2
    elif len(primelist) == 1:
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
            
def SetDigits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    return digits

def RecNumber(s):
    res = 0
    for i in range(len(s)):
        res += s[i]*10**i
    return res

def TruncCheck(n):
    s = SetDigits(n)
    for i in range(1, len(s)):
        if not DichSearch(primes, RecNumber(s[:i])) or not DichSearch(primes, RecNumber(s[-i:])):
            return False
    return True

primes = []
truncs = []
ts = time()
while len(truncs) < NUM:
    prime = NextPrime(primes)
    if prime > 10 and TruncCheck(prime):
        truncs.append(prime)
    primes.append(prime)

print sum(truncs)
print "Time:", round(time() - ts, 4)
