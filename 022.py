# What is the total of all the name scores in the file?

from time import time

def NextWord (f):
    s = []
    c = f.read(1)
    while c != '"':
        s.append(c)
        c = f.read(1)
    f.read(1)
    return s

def WordKey(s):
    res = 0
    for c in s:
        res += ord(c) - 64
    return res

ts = time()
f = open('./names.txt', 'r')
words = []
while True:
    c = f.read(1)
    if not c:
        break
    s = NextWord(f)
    words.append(s)

words.sort()
print words[:6]
res = 0
for i in range(len(words)):
    res += (i+1)*WordKey(words[i])

print res    
print "Time:", round(time() - ts, 4)

