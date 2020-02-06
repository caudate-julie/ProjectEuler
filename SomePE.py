# -*- coding: cp1251 -*-

##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##a2 + b2 = c2
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

from time import time
from random import random

def C(n, m):
    if m == 0 or m == n: return 1
    a = reduce(lambda x, y: x * y, range(1, n + 1))
    b = reduce(lambda x, y: x * y, range(1, m + 1))
    c = reduce(lambda x, y: x * y, range(1, n - m + 1))
    return a / (b * c)



def M_couples(N, d, M):
    general = d ** N
    couples = d * ((d - 1) ** (N - 1 - M)) * C(N - M, M)
    return float(couples) / general


N = 10
d = 10
M = 3
#print N, "d%d" % d
#print M, ":", "%.3f" % M_couples(N, d, M)


def NotRandom(a, limit):
    score = 0
    prev = a[0]
    chain = 2
    for c in a[1:]:
        if c == prev:
            score += chain
            chain += 1
        else:
            prev = c
            chain = 2
    if score > limit:
        print score, a

        
for i in xrange(1000):
    a = [int(random() * d) + 1 for i in xrange(N)]
    NotRandom(a, 5)


        

##t = time()
##print max(reduce(lambda x, y : x * y, A[i : i + K]) for i in xrange(N - K))
##print "Time: %.2f" % (time() - t)

    
