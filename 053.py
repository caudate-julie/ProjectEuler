# How many, not necessarily distinct, values of  (n,r),
# for 1 <= n <= 100, are greater than one-million?
# 22:52

from math import factorial
from time import time

NUM = 10**6
MAX = 101
def C(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

timestart = time()
count = 0
for n in range(MAX):
    for k in range(n):
        if C(n,k) > NUM:
            count += 1
print count
print "Time: %.4f" % (time() - timestart)
