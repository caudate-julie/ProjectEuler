# The following iterative sequence is defined for the set of positive integers:
# n n/2 (n is even)
# n  3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?

from time import time

def GetNextTerm (n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n + 1

FIN = 1
MAX = 1000000

def ChainLen (maxnumber):
    chains = [None]*maxnumber
    print len(chains)
    for n in range(1, maxnumber):
        next_term = n
        nlen = 1
        while next_term != FIN:
            next_term = GetNextTerm(next_term)
            if next_term<maxnumber and chains[next_term] is not None:
                nlen += chains[next_term]
                break
            nlen += 1
        chains[n] = nlen
    return max(chains)

ts = time()
res = ChainLen(MAX)
print "Result:", res
print "Time: %.4f" % (time() - ts)


###############################
###############################
### *** Other languages *** ###
###############################
###############################

##LISP:
##(defun collatz-sequence (start)
##  (loop for n = start then (if (evenp n)
##			       (/ n 2)
##			     (1+ (* n 3)))
##	collect n
##	until (= 1 n)))
## 
##(defun problem-14 ()
##  (loop for x from 1000000 downto 1
##	and prev-max = 0 then max
##	and num = x then (if (> max prev-max) x num)
##	maximizing (length (collatz-sequence x)) into max
##	finally (return num)))
