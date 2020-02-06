from time import time

timestart = time()
digitset = list(10**i for i in range(7))

def SetDigits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    return digits

digitnum = 0
n = 1
curdigit = 0
result = 1
while True:
    newdigits = SetDigits(n)
    digitnum += len(newdigits)
    if digitset[curdigit] <= digitnum:
        print digitset[curdigit], digitnum, newdigits
        result *= newdigits[digitnum - digitset[curdigit]]
        curdigit += 1
        if curdigit >= len(digitset):
            break
    n += 1
print result

print "Time: %.4f" % (time() - timestart)
