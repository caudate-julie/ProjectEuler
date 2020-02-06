# What is the largest 1 to 9 pandigital 9-digit number
# that can be formed as the concatenated product
# of an integer with (1,2, ... , n) where n > 1?

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

def RecNumber(s):
    res = 0
    for i in range(len(s)):
        res += s[i]*10**i
    return res

def DifDigits(s):
    if 0 in s:
        return False
    for i in range(len(s)):
        if s[i] in s[:i]+s[i+1:]:
            return False
    return True

def PanDigitalProd(n):
    m = 0
    digits = []
    for i in range(1, 10):
        if not DifDigits(SetDigits(i*n) + digits):
            return None
        digits = SetDigits(i*n) + digits
        if len(digits) == 9:
            return RecNumber(digits)

ts = time()
M = 0
for n in range(1, 100000):
    t = PanDigitalProd(n)
    if t is not None and t > M:
        M = t
        bn = n
print M, bn
print "Time:", round(time() - ts, 4)
