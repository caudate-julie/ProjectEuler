# What is the value of the first triangle number
# to have over five hundred divisors?

from time import time
from math import sqrt, ceil
from operator import mul
from itertools import count

NUM = 500

ts = time()
def AddPrime (primelist):
    if len(primelist) < 2:
        primelist.append(len(primelist) + 2)
        return primelist[-1]
    n = primelist[-1] + 2
    while True:
        t = sqrt(n)
        flag = True
        for x in primelist:
            if x > t:
                primelist.append(n)
                return n
            if n%x == 0:
                flag = False
                break
        n += 2

def primes():
    for p in primelist:
        yield p
    while True:
        yield AddPrime(primelist)

def FactorNum(n):
    factors = {}
    for p in primes():
        factors[p] = 0
        while n%p == 0:
            n /= p
            factors[p] += 1
        if n == 1:
            break
    return reduce(mul, list(x+1 for x in factors.values()))

primelist = []

for i in count(1):
    if FactorNum(i*(i+1)/2) > NUM:
        print i, i*(i+1)/2
        break

print "time: %.4f", (time() - ts)

#########################################
# Some strange and quite slowly method: #
#########################################
ts = time()
a=0; c=0; max=0; 
while max<=NUM:
    c+=1; a+=c; d=0; b=0; x=1
    while a/x != b:
        if a%x==0:
            if x*x==a:
                d+=1
                break
            b=x
            d+=2
        x+=1
    if d>max:
        max=d
        print d,a
print "time: %.4f" % (time() - ts)


###############################
###############################
### *** Other Languages *** ###
###############################
###############################

##J
##foo=:[: */ 1: + [: +/"1 =@q:
##{.(500 < foo"0 t)#t=:+/\>: i.13000

##K
##*{500>2*#&~(*x)!/:1+!__sqrt*x}{(+/x),1+x 1}/0 1

##LISP
##(defun list-divisors (n) 
##(loop for i from 1 to (sqrt n) 
##when (= (mod n i) 0) 
##collect i 
##and unless (= i (/ n i)) 
##collect (/ n i))) 
##
##(defun triangle (n) 
##(/ (* n (+ n 1)) 2)) 
##
##(defun triangle-factors (limit) 
##(loop for n from 1 
##for tri = (triangle n) 
##when (> (length (list-divisors tri)) limit) 
##return tri)) 
##
##(defun euler12 () 
##(triangle-factors 500))

