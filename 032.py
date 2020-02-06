# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

from time import time
from math import sqrt

DIG = 9

def SetDigits(n):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    return digits

def DifDigits(s, d):
    if 0 in s:
        return False
    for i in range(len(s)):
        if s[i] > d or s[i] in s[:i]+s[i+1:]:
            return False
    return True

ts = time()

def PanDigital(d):
    num = int(sqrt(10**(d/2)))
    pd = []
    for n in range(num):
        ndig = SetDigits(n)
        if not DifDigits(ndig, d):
            continue
        for m in range(n+1, num**2):
            r = n*m
            mdig = SetDigits(m)
            rdig = SetDigits(r)
            dig = mdig + ndig + rdig
            if DifDigits(dig, d) and len(dig) == d:
                print n, m, r
                if r not in pd:
                    pd.append(r)
    return pd

print sum(PanDigital(DIG))
print "Time:", round(time() - ts, 4)
