## Find the sum of all the even-valued terms
## in the Fibbonacci sequence which do not exceed four million.

a = b = 1
seqsum = 0
maxvalue = 4*(10**6)

while b < maxvalue:
    if b%2 == 0:
        seqsum += b
    a, b = b, b + a
print seqsum
