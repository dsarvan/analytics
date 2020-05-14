#!/usr/bin/env python3
import numpy as np

def fact(n):
    fact = 1
    for value in range(1, n+1):
        fact *= value
    return(fact)

n = int(input("Number of trials: "))
p = float(input("Probability of getting a success in one trail: "))
option1 = input("Type L for at least, M for at most, E for exact: ")
option2 = input("Type S for success, F for failure: ")

if option2 == 'S': x = int(input("Number of success desired: "))
else: x = int(input("Number of failure desired: "))

if option1 == 'L':
    sum = 0
    while(n >= x):
        sum += fact(n)/(fact(n-x)*fact(x)) * (p)**(x) * (1-p)**(n-x)
        x += 1

    print("{:.4f}".format(sum))
    
if option1 == 'M':
    sum = 0
    while(x >= 0):
        sum += fact(n)/(fact(n-x)*fact(x)) * (p)**(x) * (1-p)**(n-x)
        x -= 1

    print("{:.4f}".format(sum))

if option1 == 'E':
    sum = fact(n)/(fact(n-x)*fact(x)) * (p)**(x) * (1-p)**(n-x)
    print("{:.4f}".format(sum))
