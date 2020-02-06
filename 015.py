# How many routes are there through a 20*20 grid?

from math import factorial

##def factorial(n):
##    res = 1
##    for i in range(1, n):
##        res *= i
##    return res

def RoutesNumber (x, y):
    return factorial(x + y)/(factorial(x)*factorial(y))

print RoutesNumber(20, 20)
