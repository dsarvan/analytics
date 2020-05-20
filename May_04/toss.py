#!/usr/bin/env python

import numpy as np
from random import randint
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen
from num2words import num2words

print("\n____Probability of tossing coins____")
no_coin = int(input("\nEnter the number of coins: "))
option1 = input("Type L for at least, M for at most, E for exact: ")
option2 = input("Type H for Heads, T for Tails: ")

if option2 == 'H':
    side = 'Heads'
    print("[Note: Assigned value 1 for Heads and 0 for Tails]")
else:
    side = 'Tails'
    print("[Note: Assigned value 0 for Heads and 1 for Tails]")

data = []
numTrails = 10_00_000

for m in range(numTrails):
    flips = [randint(0,1) for n in range(no_coin)]

    if option2 == 'H':
        for n in flips:
            if n == 1: data.append(1)
            else: data.append(0)

    if option2 == 'T':
        for n in flips:
            if n == 0: data.append(1)
            else: data.append(0)

data = np.array([data[i:i + no_coin] for i in range(0, len(data), no_coin)]).tolist()
sample_space = list(unique_everseen(duplicates(data)))
length = len(sample_space)
print("\nThe sample space has {} total number of outcomes: \n{}".format(length, sample_space))

if option1 == 'L':
    lvalue = int(input("\nAt least number of {}: ".format(side)))

    count = 0
    for _list_ in sample_space:
        sum = 0
        for n in _list_:
            sum += n

        if sum >= lvalue: count += 1

    lvalue = num2words(lvalue)

    print("The Probability of getting at least {} {} = {}\n".format(lvalue, side, count/length))

elif option1 == 'M':
    mvalue = int(input("\nAt most number of {}: ".format(side)))

    count = 0
    for _list_ in sample_space:
        sum = 0
        for n in _list_:
            sum += n

        if sum <= mvalue: count += 1

    mvalue = num2words(mvalue)

    print("The Probability of getting at most {} {} = {}\n".format(mvalue, side, count/length))

else:
    evalue = int(input("\nExact number of {}: ".format(side)))
 
    count = 0
    for _list_ in sample_space:
        sum = 0
        for n in _list_:
            sum += n

        if sum == evalue: count += 1

    evalue = num2words(evalue)

    print("The Probability of getting exactly {} {} = {}\n".format(evalue, side, count/length))
