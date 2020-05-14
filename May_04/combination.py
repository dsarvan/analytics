#!/usr/bin/env python3

def fact(n):
    fact = 1
    for value in range(1,n+1):
        fact *= value
    return(fact)

def nCr(n,r):
    return(fact(n)/(fact(n-r)*fact(r)))

print("__n choose r__")
n = int(input("n: "))
r = int(input("r: "))
print("C({},{}) = {}".format(n, r, nCr(n,r)))
