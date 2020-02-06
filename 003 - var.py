from math import sqrt
from time import time

time()
print

# Not my solution
ts = time()
number = 600851475143
divisor = 2
while number > 1:
    if number % divisor == 0:
        number /= divisor
        divisor -= 1
    divisor += 1
print divisor
print "Time: %.6f" % (time() - ts)


# Also not my solution
ts = time()
d, n = 3, 600851475143 
while (d * d < n):
    if n % d == 0: n /= d
    else: d += 2 
print n
print "Time: %.6f" % (time() - ts)


## *** Other languages ***

## HASKELL
##prime_factors_of :: Integer -> [Integer]
##prime_factors_of 0 = []
##prime_factors_of 1 = []
##prime_factors_of n = f : prime_factors_of(n `div` f)
##where f = head $ filter (\d -> n `mod` d == 0) [2..n]

## LISP
##(defun find-largest-prime-divisor (n)
##  (do ((i (floor (sqrt n)) (decf i)))
##      ((and (= 0 (mod n i)) (primep i)) i)))
## 
##(defun primep (n)
##  (cond ((= 2 n) t)
##	((evenp n) 'nil)
##	(t (let ((limit (floor (sqrt n))))
##	     (do ((i 3 (incf i 2)))
##		 ((> i limit) t)
##	       (if (= 0 (mod n i)) (return-from primep 'nil)))))))
## 
##(find-largest-prime-divisor 317584931803)

## HASKELL
##mind x = head [y | y <- [2..], x `mod` y == 0] 
##factorize 1 l = l 
##factorize p l = factorize (p `div` (mind p)) l++[mind p] 
##head (factorize 317584931803 [])

#include <iostream> 

## C++
##int main() {
##    long long number = (long long)(317584931803.0);
##    for (long long div = 3; div != number; div += 2) {
##        while (number % div == 0) number /= div;
##    } 
##
##std::cout << number << std::endl; 
##}
