# Find the greatest product of five consecutive digits in the 1000-digit number.
from time import time

a = "73167176531330624919225119674426574742355349194934" + \
    "96983520312774506326239578318016984801869478851843" + \
    "85861560789112949495459501737958331952853208805511" + \
    "12540698747158523863050715693290963295227443043557" + \
    "66896648950445244523161731856403098711121722383113" + \
    "62229893423380308135336276614282806444486645238749" + \
    "30358907296290491560440772390713810515859307960866" + \
    "70172427121883998797908792274921901699720888093776" + \
    "65727333001053367881220235421809751254540594752243" + \
    "52584907711670556013604839586446706324415722155397" + \
    "53697817977846174064955149290862569321978468622482" + \
    "83972241375657056057490261407972968652414535100474" + \
    "82166370484403199890008895243450658541227588666881" + \
    "16427171479924442928230863465674813919123162824586" + \
    "17866458359124566529476545682848912883142607690042" + \
    "24219022671055626321111109370544217506941658960408" + \
    "07198403850962455444362981230987879927244284909188" + \
    "84580156166097919133875499200524063689912560717606" + \
    "05886116467109405077541002256983155200055935729725" + \
    "71636269561882670428252483600823257530420752963450"

NUM = 5

#################################
# My variant (renewed in 2016): #
#################################

def Prod(a):
    res = 1
    for x in a:
        res *= int(x)
    return res

def Sequence_2(a):
    return max(Prod(a[i-NUM:i]) for i in range(NUM, len(a)+1))

ts = time()
print Sequence_2(a)
print "Time:", time()-ts

###################
# Not my variant: #
# (it's faster)   #
###################
from string import whitespace
from operator import mul

ts = time()
data = open('8.txt') # Number pasted to file.
nos = [int(c) for line in data for c in line if c not in whitespace]
print max([reduce(mul, nos[i:i+NUM]) for i in range(len(nos)-NUM)])
print "time: %f" % (time()-ts)

########################
# This is with lambda: #
########################
b = ''    # this is for me not to retype.
for x in a:
    if x not in whitespace:
        b += x

def test():
    ns = b
    p = 1
    for i in range(0, len(ns) - 4):
        p = max(reduce(lambda x, y: x * y, map(int, ns[i:i+5])), p)
    print p

ts = time()
test()
print "Time:", time()-ts


###############################
###############################
### *** Other languages *** ###
###############################
###############################

## J (number into y)
##>./>([:*/10 10 10 10 10"_ #:[:".])&.>5<\y

## J (number into q)
##>./5*/\"."0 q

## J (number into y)
##>./*/"1]5"."0\y-.LF

##LISP
##(defparameter *bignumber* "7316717[etc]") 
##
##(defun char-to-int (c) 
##(- (char-code c) 48)) 
##
##(defun f (s) 
##(let ((output 0)) 
##(dotimes (i (- (length s) 5) output) 
##(let ((currentprod 
##(reduce #'* (mapcar (lambda (j) (char-to-int (aref s (+ i j)))) '(0 1 2 3 4))))) 
##(if (> currentprod output) 
##(setf output currentprod)))))) 
##
##(f *bignumber*)

## LISP
##(defun getProduct (x prod) 
##(if (< (length x) 5) prod 
##(let ( (newprod (getProd x)) ) 
##(if (> newprod prod) (getProduct (subseq x 1) newprod) 
##(getProduct (subseq x 1) prod) 
##)))) 
##
##(defun getProd (x) 
##(* (digit-char-p (char x 0)) (digit-char-p (char x 1)) (digit-char-p (char x 2)) (digit-char-p (char x 3)) (digit-char-p (char x 4)) ) 
##)

##LISP
##(defun digit-list (n)
##  (labels ((digit-list-r (n)
##             (if (< n 10)
##                 (list n)
##                 (cons (mod n 10)
##                       (digit-list-r (floor (/ n 10)))))))
##    (nreverse (digit-list-r n))))
##(loop for x on (digit-list <long number>)
##      maximize (apply #'* (subseq x 0 5)))

##LISP
##(let ((a "7316...3450")) 
##(loop for b from 0 to (- (length a) 6) maximizing 
##(reduce #'* 
##(map 'vector (lambda(x) (- (char-code x) 48)) 
##(subseq a b (+ b 5))))))
