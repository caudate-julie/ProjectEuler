# What is the largest n-digit pandigital prime that exists?

from time import time
from math import sqrt

def PanDigitalCheck(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n /= 10
    return sorted(digits) == list(range(1, len(digits)+1))

def PanDigitalPrime():
    if len(primelist) == 0:
        primelist.append(2)
        return
    if len(primelist) == 1:
        primelist.append(3)
        return
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
            primelist.append(n)
            if PanDigitalCheck(n):
                return n
            else:
                return
        n += 2
    return

primelist = [2]
timestart = time()
result = 0

print PanDigitalCheck(2143)

while primelist[-1] < 10**8:
    if len(primelist)%8000 == 0:
        print "Current:", primelist[-1]
    t = PanDigitalPrime()
    if t is not None:
        result = t
print "Result:", result
print round(time() - timestart, 4)
