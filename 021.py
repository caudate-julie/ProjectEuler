# Evaluate the sum of all the amicable numbers under 10000.

from time import time
from math import sqrt

def factorSum(n):
    s = 1
    for d in range(2, sqrt(n)+1):
        if n%d == 0:
            s += d
            if d != sqrt(n):
                s += n/d
    return s

def amicNum(NUM):
    result = 0
    for n in range(1, NUM):
        m = factorSum(n)
        if m != n and n == factorSum(m):
            result += n
    return result

NUM = 10000
ts = time()
amicNum(NUM)
print "Time:", round(time() - ts, 4)

#############
# Not mine: #
#############

ts = time()

def divsum(n):return sum([k+n/k for k in range(1,int(n**.5 + 1)) if n%k == 0])-n
sum([n for n in range(1,NUM) if n==divsum(divsum(n)) if n!=divsum(n)])

print "Time:", round(time() - ts, 4)
