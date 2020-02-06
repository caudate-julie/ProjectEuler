# Find the last ten digits of the series,
# 1^1 + 2^2 + 3^3 + ... + 1000^1000.
# 21:03 - 21:42

from time import time

N = 10**10

def LastDigits(N, a, k):
    tails = [1]
    flag = True
    for i in range(k):
        newtail = (tails[-1]*a)%N
        if newtail not in tails:
            tails.append(newtail)
        else:
            start = tails.index(newtail)
            cycle = len(tails) - start
            flag = False
            break
    if flag:
        return tails[-1]
    else:
        return tails[(k-start)%cycle + start]

timestart = time()
r = sum(LastDigits(N, i, i) for i in range(1, 1001))
print "Result:\n", r%N
print "Time: %.4f" % (time() - timestart)
