# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from time import time

RES = 1000

###############
# My old one: #
###############
def Pythagoreans():
    a = 1
    tres = RES/2 + 1
    for a in range(1, tres):
        for b in range (a, tres):
            c = RES - a - b
            if c*c == a*a + b*b:
                #print a, b, int(c)
                return a*b*int(c)
##    print "No way..."
##    return None

ts = time()
Pythagoreans()
print "Time: %.4f" % (time() - ts)

################
# Another way: #
################
def solving():
    for c in xrange(RES/3, RES/2):
        for a in xrange(1, (RES-c)/2):
            b = (RES - c) - a
            if a**2 + b**2 == c**2:
                #print "a,b,c =",a,b,c
                return

ts = time()
solving()
print "Time: %.4f" % (time() - ts)


###############################
###############################
### *** Other languages *** ###
###############################
###############################

## Ruby
##n = 1000
##a = (1..n / 2).to_a.find { |a|
##  (n * (n / 2 - a) % (n - a)).zero?
##}
##b = n * (n / 2 - a) / (n - a)
##puts "Product is #{a * b * (n - a - b)}."

##K
##*/_*a@&1000=+/'a:b,'(_sqrt+/)'b*b:,/n,/:'1+!:'n:!1000

##LISP
##(defun euler9 () 
##(car 
##(loop for a from 1 to 998 
##append (loop for b from 1 to (- 999 a) 
##append (let ((c (- 1000 a b))) 
##(if (= (* c c) 
##(+ (* a a) (* b b))) 
##(list (* a b c))))))))

##J: 
##x:*/{.(#~ 1000"_=+/"1)(, +&.*:/)"1,/,"0/~1+i.1000

    
