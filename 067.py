from time import time

inpath = 'triangle.txt'
timestart = time()
f = open(inpath, 'r')
lines = f.readlines()
f.close
triangle = list(map(int, x.split()) for x in lines)
for i in reversed(range(len(triangle)-1)):
    for j in range(i+1):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
print triangle[0][0]
print "Time: %.4f" % (time() - timestart)
