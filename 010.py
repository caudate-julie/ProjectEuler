# Find the sum of all the primes below two million.
from time import time
from operator import mul
from math import sqrt

MAX = 2000000

def NextPrime (primelist):
    if len(primelist) < 2:
        return 2 + len(primelist)
    n = primelist[-1] + 2
    while True:
        t = sqrt(n)
        flag = True
        for x in primelist:
            if x > t: break
            if n%x == 0:
                flag = False
                break
        if flag: return n
        n += 2

primelist = []
primesum = 0
timestart = time()

while True:
    x = NextPrime(primelist)
    if x > MAX: break
    primelist.append(x)
    primesum += x

print primesum
print "time: %.4f" % (time() - timestart)

#############################
# 5 times faster, not mine, #
# eats up lots of memory    #
#############################

def sumofprimes(m = MAX):
    bucket = range(m+1)
    bucket[1] = 0
    for i in bucket:
        if i > 0:
            for not_prime in xrange(2*i, m+1, i):
                bucket[not_prime] = 0
    return sum(bucket)

timestart = time()
print sumofprimes()
print "time: %.4f" % (time() - timestart)

###############################
###############################
### *** Other languages *** ###
###############################
###############################

## J
##+/ p: i. x: pi 1e6

## C++
##I combined the advantages of asm and C++ by using bits
##for the Eratosthenes Sieve storage and the expressiveness
##of C++ into an elegant soloution. However, it still has
##the same brute force solution at heart. 
##
###include <iostream> 
###include <bitset> 
##
##using namespace std; 
##
##int main() 
##{ 
##  bitset<1000000> Sieve; 
##  __int64 sum = 0; 
##
##  Sieve.flip();    // Set all bits to 1 
##  Sieve[0].flip();  // Set 0 and 1 to not prime 
##  Sieve[1].flip(); 
##
##  // Check all nos from 2 to 1 million 
##  for(long i = 2; i < 1000000; ++i) 
##  { 
##    if( ! Sieve )  // If marked not prime 
##      continue;    // return to head of loop 
##    else 
##      // Set all multiples as not prime 
##      for(long j = 2*i; j < 1000000; j += i) 
##        Sieve[j] = 0; 
##  } 
##
##  for(long i = 2; i < 1000000; ++i) 
##    if( Sieve )  // Add all nos with bit set 
##      sum += i; 
##
##  cout << "\nThe sum is : " << sum << endl; 
##
##  return 0; 
##} 
##The program leaves all the prime numbers with their
##bit values set to 1 and this allows later testing
##and addition. This is a very useful way to generate
##all primes in a given range.

## LISP
##(defun euler10 (&optional (sieve 1000000))
##  (let ((numbers (make-array sieve :initial-element t))
##        (upper-bound (isqrt (- sieve 1)))
##        (total 0))
##    (do ((i 2 (+ i 1))) ((> i upper-bound) 'done)
##      (when (svref numbers i)
##        (incf total i)
##        (do ((j (* i i) (+ j i))) ((> j (- sieve 1)) 'done)
##          (setf (svref numbers j) nil))))
##    (do ((i (+ 1 upper-bound) (+ i 1))) ((= i sieve) total)
##      (when (svref numbers i)
##	(incf total i)))))

