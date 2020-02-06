# What is the sum of both diagonals in a 1001 by 1001 spiral
# formed in the same way?

from time import time

MAXLEN = 1001
curlen = 0
dsum = 1
curnum = 1
for currow in range(1, (MAXLEN+1)/2):
    curlen += 2
    for i in range(4):
        curnum += curlen
        dsum += curnum
print dsum
        
ts = time()

print "Time:", round(time() - ts, 4)
