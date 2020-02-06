# How many circular primes are there below one million?

from math import sqrt
from time import time
from copy import deepcopy
from bisect import bisect_left

MAX = 1000000

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

def RecNumber(s):
    res = 0
    for i in range(len(s)):
        res += s[i]*10**i
    return res

def SetDigits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    return digits

def CircularCheck(n):
    s = SetDigits(n)
    pl = len(primelist)
    for x in list(s[i:]+s[:i] for i in range(len(s))):
        t = RecNumber(x)
        place = bisect_left(primelist, t)
        if  place == pl or primelist[place] != t:
            return False
    return True

ts = time()
primelist = [2]
while primelist[-1] < MAX:
    primelist.append(NextPrime(primelist))
del primelist[-1]
print "Primes:", len(primelist), "last:", primelist[-1]
#circularnum = sum(1 for x in primelist if CircularCheck(x))
circularnum = 0
for i in range(len(primelist)):
    if CircularCheck(primelist[i]):
        circularnum += 1
print "Result:", circularnum
print "Time:", round(time() - ts, 4)
