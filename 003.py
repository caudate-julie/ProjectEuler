# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from math import sqrt
from time import time

ts = time()
number = 80600851475143
nrow = list(range(int(sqrt(number))+ 1))
nrow[1] = 0
l = len(nrow)
factors = []
i = 2
while number > 1 and i < l:
    if nrow[i] != 0:
        j = 2*i
        while j < l:
            nrow[j] = 0
            j += i
        while number%i == 0:
            factors.append(i)
            number /= i
    i += 1
factors.append(number)

result = max(factors)
print result, factors, round(time() - ts, 4)
# the only thing I can't understand is - why does it append L
# to the last 1?
            
