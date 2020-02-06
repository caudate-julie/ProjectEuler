# What is the smallest number that is evenly divisible
# by all of the numbers from 1 to 20?

from time import time
from math import sqrt

NUM = 3000

###########
# My code #
###########
def LCM (m, n):
    while b != 0:
        a, b = b, a % b
    return a 

ts = time()
result = reduce(LCM, range(1, NUM+1))
#print result
print "time: %.6f" % (time() - ts)

########################
# Not my code.         #
# (slowlier than mine) #
########################
ts = time()
i = 1 
for k in (range(1, NUM+1)):
    if i % k > 0:
        for j in range(1, NUM+1):
            if (i*j) % k == 0:
                i *= j
                break 
#print i
print "time: %.6f" % (time() - ts)

################################
# Another one not mine:        #
# (~30 times faster than mine) #
################################
ts = time()
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a 

def lcm(a, b):
    return a*b/gcd(a, b) 

result = reduce(lcm, range(1, NUM+1))
#print result
print "time: %.6f" % (time() - ts)



###############################
###############################
### *** Other languages *** ###
###############################
###############################

## J
##[code]*./>:i.20

## K
##{_ x*y%{:[~x;y;_f[y;x!y]]}[x;y]}/1+!20

## Lisp
##(defun full-lcm (limit) 
##(apply #'lcm (loop for i from 1 to limit collect i))) 
##
##(defun euler5 () 
##(full-lcm 20))

## J without *. 
##*/ ((>./"1@(+/@(E.&>)/) # [)~ ~.@;) <@q: 1+i.20
## one more:
##*/(p:i.8)^>./8 q:>:i.20x

## Haskell:
##foldl (lcm) 1 [1..20]

