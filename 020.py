# Find the sum of the digits in the number 100!
from math import factorial

NUM = 100
a = str(factorial(NUM))
result = 0
for x in a:
    result += int(x)
print result
