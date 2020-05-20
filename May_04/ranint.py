#!/usr/bin/env python3
import numpy as np

print("\n_An integer is chosen at random out of the integers from 1 to 100_\n")

numTrails = 10_00_000

data = []
for n in range(numTrails):
    data.append(np.random.randint(1, 101, size=1))

sample_space = np.unique(data)
total_outcome = len(sample_space)
minValue = min(sample_space)
maxValue = max(sample_space)

print("The Sample space has {} total number of outcomes: \n{}".format(total_outcome,  sample_space))

option1 = input("\nType M for multiples, L for lesser than, G for greater than: ")
if option1 == 'M': chosen = 'multiples of'
elif option1 == 'L': chosen = 'lesser than'
else: chosen = 'greater than'
option2 = int(input("Enter an integer for which to find values that are {}: ".format(chosen)))

values = []
for num in sample_space:
    if option1 == 'M':
        if num%option2 == 0: values.append(num)
    elif option1 == 'L':
        if num < option2: values.append(num)
    else:
        if num > option2: values.append(num)

total = len(values)

print("\nFrom {} to {}, there are {} integers that are {} {}: \n{}".format(minValue, maxValue, total, chosen, option2, values))
print("\nThe Probability that an integer is {} {}: {}\n".format(chosen, option2,  total/total_outcome))
