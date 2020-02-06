# Find the sum of all 0 to 9 pandigital numbers with this property.
# 17:26 - 17.45

from time import time
primes = (0, 1, 2, 3, 5, 7, 11, 13, 17)

def PropertyCheck(a):
    for i in range(2, 9):
        if (a[-i]*100 + a[-i-1]*10 + a[-i-2])%primes[i] != 0:
            return False
    return True

def DepthPermutation(a, result):
    if len(a) == 8:
        print a, result
    if len(a) == 0:
        if PropertyCheck(result):
            return sum(result[i]*10**i for i in range(10))
        else:
            return 0
    else:
        return sum(DepthPermutation(a[:i]+a[i+1:], [a[i]]+result) for i in range(len(a)))

timestart = time()
print DepthPermutation(list(range(10)), [])
print "Time: %.4f" % (time() - timestart)
