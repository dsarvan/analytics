#!/usr/bin/env python3

def fact(n):
    fact = 1
    for value in range(1,n+1):
        fact *= value
    return(fact)

print("__Factorial__")
n = int(input("Number: "))
print("Factorial of {} is {}".format(n, fact(n)))
