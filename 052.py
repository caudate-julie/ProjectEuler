# ind the smallest positive integer, x,
# such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# 22:43 - 22:50

from time import time

NUM = 6
def SetDigits(n):
    digits = []
    while n>0:
        digits.append(n%10)
        n /= 10
    return digits

timestart = time()
flag = True
n = 1
while flag:
    n += 1
    d = sorted(SetDigits(n))
    flag = False
    for k in range(2, NUM+1):
        if sorted(SetDigits(n*k)) != d:
            flag = True
            break


print n
print "Time: %.4f" % (time() - timestart)
