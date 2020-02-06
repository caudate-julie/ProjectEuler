# What is the millionth lexicographic permutation
# of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial
from time import time

def Permutations(a, ordnum):
    seq = list(range(a))
    n = len(seq)
    pnum = [0]*(n-1)
    seq.sort()
    for i in range(1, n):
        pnum[i-1] = factorial(n-i)
    trans = [0]*(n-1)
    t = 0
    for i in range(1, n):
        j = 0
        while t <= ordnum-1 and (i == 1 or j < pnum[i-2]):
            t += pnum[i-1]
            j += 1
        t -= pnum[i-1]
        j -= 1
        trans[i-1] = j
    for i in range(n-1):
        t = seq[i]
        seq[i] = seq[i+trans[i]]
        seq[i+trans[i]] = t
        seq[(i+1):] = sorted(seq[(i+1):])
    return seq

LEN = 10
ORD = 1000000

ts = time()
print Permutations(LEN, ORD)
print "Time:", round(time() - ts, 4)
