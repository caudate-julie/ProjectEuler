# -*- coding: utf-8 -*-
# How many different ways can £2 be made using any number of coins?

from time import time

COINS = (200, 100, 50, 20, 10, 5, 2, 1)
COINNUM = len(COINS) - 1
MONEY = 200

def CoinIter(rest, n):
    if n == COINNUM:
        if rest%COINS[n] == 0:
            return 1
        else:
            return 0
    number = 0
    for m in reversed(range(rest/COINS[n]+1)):
        number += CoinIter(rest - m*COINS[n], n+1)
    return number 

ts = time()
print CoinIter(MONEY, 0)
print "Time:", round(time() - ts, 4)
