# How many are triangle words?
# 17:12 - 17:23

from time import time
inpath = '042.txt'

def NewTriangle():
    n = len(triangles)
    triangles.append(n*(n+1)/2)
    return

timestart = time()
f = open(inpath, 'r')
wordline = f.readline()
f.close
flag = False
words = []
triangles = [1]
trianglewords = 0
for c in wordline:
    if c == '"':
        if flag:
            words.append(newword)
        else:
            newword = []
        flag = not flag
    else:
        if flag:
            newword.append(c)
for w in words:
    wnumber = 0
    for c in w:
        wnumber += ord(c) - ord('A') + 1
    while triangles[-1] < wnumber:
        NewTriangle()
    if wnumber in triangles:
        trianglewords += 1
print "Result:\n", trianglewords
print "Time: %.4f" % (time() - timestart)
