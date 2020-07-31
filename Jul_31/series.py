#!/usr/bin/env python3

import numpy as np

def factorial(num):
    value = 1
    while (num >= 1):
        value *= num
        num = num - 1
    return value

def sin(x):
    sum = 0
    for n in range(99):
        sum += ((-1**n)/factorial(2*n+1))*(x**(2*n+1))
    return sum

print(sin(30))
print(np.sin(30))
