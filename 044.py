# Find the pair of pentagonal numbers, Pj and Pk,
# for which their sum and difference is pentagonal
# and D = |Pk - Pj| is minimised; what is the value of D?

from time import time
from bisect import bisect_left

P = [1]
print "Go!"

def PentagonalCheck(n):
    while P[-1] < n:
        NextPentagonal()
    return P[bisect_left(P, n)] == n

def NextPentagonal():
    n = len(P)+1
    P.append(n*(3*n-1)/2)
    return

timestart = time()
k = 0
flag = True
while flag:
    k += 1
    if k%100 == 0:
        print k/100, "curtime: %.4f" % (time() - timestart)
    NextPentagonal()
    for j in range(k):
        if PentagonalCheck(P[k]+P[j]):
            if PentagonalCheck(2*P[k]+P[j]):
                flag = False
                print "P[%d] = %d, P[%d] = %d" % (j+k,P[j]+P[k],k,P[k])

##i = j
##D = P[j]
##while P[k+1]-P[k] < D:
##    k += 1
##    if k%100 == 0:
##        print k/100, "curtime: %.4f" % (time() - timestart)
##    NextPentagonal()
##    for j in range(i):
##        if PentagonalCheck(P[k]+P[j]):
##            if PentagonalCheck(P[k], P[k]+P[j]):
##                flag = False
##                D = P[j]
##                i = j
##                print "P[%d] = %d, P[%d] = %d" % (j+k, P[j]+P[k], k, P[k])
##                print D
        
print "Time: %.4f" % (time() - timestart)
