#!/usr/bin/env python3
import math
import numpy as np

print("\n__________Poisson Distribution__________\n")
mu = float(input("Number lambda: "))
option = input("Type L for at least, M for at most, E for exact,\
 LT for less than, MT for more than: ")

if option == 'L':
    k = int(input("Number of at least: "))
    sum = 0
    for n in range(k):
        sum += (mu)**n*np.exp(-mu)/math.factorial(n)

    sum = 1-sum
    print("\nProbability: {:.4f}\n".format(sum))

if option == 'M':
    k = int(input("Number of at most: "))
    sum = 0
    while(k >= 0):
        sum += (mu)**k*np.exp(-mu)/math.factorial(k)
        k -= 1

    print("\nProbability: {:.4f}\n".format(sum))

if option == 'E':
    k = int(input("Number of exact: "))
    sum = (mu)**k*np.exp(-mu)/math.factorial(k)
    print("\nProbability: {:.4f}\n".format(sum))

if option == 'LT':
    k = int(input("Number of less than: "))
    sum = 0
    for n in range(k):
        sum += (mu)**n*np.exp(-mu)/math.factorial(n)

    sum = 1-sum
    sum = 1-sum
    print("\nProbability: {:.4f}\n".format(sum))

if option == 'MT':
    k = int(input("Number of more than: "))
    sum = 0
    while(k >= 0):
        sum += (mu)**k*np.exp(-mu)/math.factorial(k)
        k -= 1

    sum = 1-sum
    print("\nProbability: {:.4f}\n".format(sum))
