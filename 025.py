# What is the first term in the Fibonacci sequence to contain 1000 digits?

from time import time

NUM = 1000

ts = time()
a = b = 1
count = 2
while True:
    c = a + b
    count += 1
    if c/(10**(NUM-1)) > 0:
        print count
        break
    if a > b:
        b = c
    else:
        a = c
print "Time:", round(time() - ts, 4)
