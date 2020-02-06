# What is the 10001st prime number?
from time import time
from math import sqrt
from itertools import count

NUM = 100000

#####################
# Mine the old one: #
#####################
def NextPrime (primelist):
    if len(primelist) < 2:
        return len(primelist) + 2
    n = primelist[-1] + 2
    while True:
        t = sqrt(n)
        flag = True
        for x in primelist:
            if x > t:
                break
            if n%x == 0:
                flag = False
                break
        if flag:
            return n
        n += 2

primelist = []
timestart = time()
for i in range(NUM):
    primelist.append(NextPrime(primelist))

#print primelist[-1]
print round(time() - timestart, 4)

######################################
# My new is slowlier on big numbers: #
######################################
ts = time()
i = 1
for x in count(3):
    if x%2 == 0:
        continue
    if all(x%d > 0 for d in range(3, sqrt(x)+1)):
        i += 1
    if i == NUM:
#        print x
        break
print "%.4f" % (time() - ts)

#################################################
# Not mine, slowlier than 1st, faster than 2nd: #
#################################################

s = time() 
def IsPrime( n ):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    i = 3
    rang = int( sqrt(n) ) + 1
    while( i < rang ):
        if( n % i == 0):
            return 0
        i += 1
    return 1

N,T = 1,3 
while N < NUM:
    if IsPrime(T):
        N+=1
    T+=2 
#print T-2 
print time() - s




