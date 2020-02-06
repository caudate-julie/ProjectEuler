# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

from time import time

MAX = 100
power = 2

ts = time()
sumofpowers = sum(x**power for x in range(MAX + 1))
powerofsums = sum(range(MAX + 1))**power
result = powerofsums - sumofpowers
print result, "- time:", round(time() - ts, 4)

# I could write it in fewer lines,
# but whether it is better?
