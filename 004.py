from time import time
MAX = 999

# My new decision
def PalindromeSearch (MAX):
    flag = True
    palindrome = 0
    for f1 in range(MAX, 1, -1):
        if f1*MAX < palindrome:
            break
        for f2 in range(MAX, f1-1, -1):
            prod = f1*f2
            if str(prod) == str(prod)[::-1] and prod > palindrome:
                palindrome = prod
                pair = (f1, f2)
                break
    print "Result:", palindrome, pair
    return palindrome

ts = time()
PalindromeSearch (999)
print "time: ", round(time() - ts, 4)


# Not my variant:
max([x*y for x in range(900,1000) for y in range(900,1000)
     if str(x*y) == str(x*y)[::-1]])


# checked on 3, 4, 5, 6 & 7 digits
# only for 3 the result is not the first found
# either there's no check of existing...


###############################
###############################
### *** Other languages *** ###
###############################
###############################

## J:
##>([:{: ]#~ (=|.&.>)) <@":"0 /:~(0:-.~[:,>:/**/)~(i.100)-.~i.1000

## J:
##|/m@&{x~|x}'$m:,/n*/:\:n:!1000

## J: 
##>./(#~ (-: |.)@":"0) ,/*/~i.1000

## K:
##|/m@&{x~|x}'10_vs'm:*/',/n,/:\:n:100+!900

## Haskell
##[m | a <- [9], b <- [0..9], c <- [0..9], m <- [100001* a + 10010 * b + 1100 * c], [x | x <- [100..999], m `mod` x == 0 && m `div` x < 1000] /= []]

## Haskell:
##> let palindrome x = let digits = show x in 
##digits == reverse digits 
##> maximum [x * y | x <- [100..999], y <- [100..999], 
##palindrome (x * y)]

## LISP:
##(defun euler4 (&optional (n 999))
##  (let ((largest 0))
##    (do ((i 1 (+ i 1))) ((> i n) largest)
##      (do ((j 1 (+ j 1))) ((> j n) 'done)
##        (if (and (> (* i j) largest)
##                 (string= (format nil "~A" (* i j))
##                          (reverse (format nil "~A" (* i j)))))
##            (setf largest (* i j)))))))

