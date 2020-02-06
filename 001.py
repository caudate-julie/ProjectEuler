## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Find the sum of all the multiples of 3 or 5 below 1000.
from time import time

multiples = []
S = 0
MAX = 1000
divs = [3, 5]

time_start = time()

## bad way: making a list with revisions. 5.5 secs for 50 000

##for x in divs:
##    n = x
##    while n < MAX:
##        if n not in multiples:
##            multiples.append(n)
##        n += x
##for x in multiples:
##    S += x

def arithm_sum(d, M):
    n = M / d
    return d * n * (n + 1) / 2

## better way. Inclusion-exclusion formula and arithmetic sums.
## 0.02 secs for 50 000
for i in range(1, 2 ** len(divs)):
    product = 1
    sign = -1
    for j in range(len(divs)):
        if not 2 ** j & i == 0:
            product *= divs[j]
            sign *= -1
    S += sign * arithm_sum(product, MAX)       
        

print "Sum:", S
print "Time: %.2f" % (time() - time_start)


