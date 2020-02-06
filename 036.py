# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.

from time import time
MAX = 1000000

def BasePalindromeCheck (n, base):
    digits = []
    while n != 0:
        digits.append(n%base)
        n /= base
    for i in range(len(digits)/2):
        if digits[i] != digits[-i-1]:
            return False
    return True


ts = time()
print sum(n for n in range(MAX)
          if BasePalindromeCheck(n, 10) and BasePalindromeCheck(n, 2))
print "Time:", round(time() - ts, 4)
