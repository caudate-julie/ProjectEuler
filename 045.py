# Find the next triangle number that is also pentagonal and hexagonal.
# 22:34 - 22:53

from time import time
from math import sqrt

PREV = 143

def TriangleCheck(n):
    return (-1 + sqrt(1 + 8*n))/2 == int((-1 + sqrt(1 + 8*n))/2)

def PentagonalCheck(n):
    return (1 + sqrt(24*n + 1))/6 == int((1 + sqrt(24*n + 1))/6)

timestart = time()
print "Go!"
k = PREV
while True:
    k += 1
    hexnumber = k*(2*k - 1)
    if PentagonalCheck(hexnumber):
        print hexnumber
        if TriangleCheck(hexnumber):
            break

print
print k
print hexnumber
print "Time: %.4f" % (time() - timestart)
