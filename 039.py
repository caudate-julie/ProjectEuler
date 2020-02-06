# For which value of p  1000, is the number of solutions maximised?

from time import time

MAX = 1000

timestart = time()
maxsolutions = 0
print "Go!"
for p in range(MAX+1):
    if p%100 == 0:
        print "progress:", p/10, '%'
    solutions = 0
    for a in range(p/3):
        for b in range(a, p/2):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solutions += 1
    if solutions > maxsolutions:
        maxsolutions = solutions
        result = p

print result       
print "Time: %.4f" % (time() - timestart)
