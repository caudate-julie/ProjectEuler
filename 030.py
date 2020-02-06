# Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits.

from time import time
POW = 5

ts = time()
tn = 1
while 10**tn <= (9**POW)*tn:
    tn += 1
DEG = 10**tn

def SetDigits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    return digits

def DPSum (n):
    return n == sum(a**POW for a in SetDigits(n))

res = 0
for n in range(2, DEG):
    if DPSum(n):
        res += n

print res
print "Time:", round(time() - ts, 4)
