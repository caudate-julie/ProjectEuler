# If all the numbers from 1 to 1000 (one thousand) inclusive
# were written out in words, how many letters would be used?

from time import time

WORDSET = [
    ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
    ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
     'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],
    ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'],
    ]    

DIGITSET = ['hundred', 'thousand', 'million', 'billion']

def SetDigits(n):
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    while len(digits)%3 != 0:
        digits.append(0)
    return digits

def HundredWord(seq):
    word = ['']*3
    for i in (0, 1, 2):
        word[i] = WORDSET[0][seq[i]]
    if seq[1] == 1:
        word[2] = ''
        word[1] = WORDSET[1][seq[2]]
    elif seq[1] != 0:
        word[1] = WORDSET[2][seq[1]]
    if seq[0] != 0:
        word[1:1] = [DIGITSET[0]]
    return word

def GetWord(n):
    digits = SetDigits(n)
    word = []
    for i in range(len(digits)/3):
        curword = HundredWord(list(reversed(digits[3*i:3*(i+1)])))
        if i > 0:
            curword.append(DIGITSET[i])
        word[:0] = curword
    if sum(digits[:2]) != 0 and sum(digits[2:]) != 0:
        word[-2:-2] = ['and']
    return word

def WordLen(n):
    word = GetWord(n)
    lenght = 0
    for x in word:
        lenght += len(x)
    return lenght

NUM = 1000
result = 0
ts = time()
for n in range(1, NUM+1):
    result += WordLen(n)
print result
print "Time:", round(time() - ts, 4)

##while True:
##    n = input()
##    print GetWord(n)
