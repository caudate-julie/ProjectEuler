# Find the value of d < 1000 for which 1/d contains
# the longest recurring cycle in its decimal fraction part.

from time import time
def RecCycle(d):
    cycle = []
    a = 1
    while True:
        b = a/d
        a = (a%d)*10
        if (a, b) in cycle:
            le = cycle.index((a, b))
            re = len(cycle)
            return re - le
        cycle.append((a, b))

MAX = 1000
ts = time()
mc = 0
iterval = 1000
for d in range(1, MAX):
    if d%iterval == 0:
        print d/iterval
    nc = RecCycle(d)
    if nc > mc:
        mc = nc
        md = d
print md, '-', mc
print "Time:", round(time() - ts, 4)
