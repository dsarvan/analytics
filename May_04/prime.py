#!/usr/bin/env python3

import numpy as np
import sympy as sp

data = list(sp.primerange(1, 1000))
print("Generate prime number till 1000: \n{}\n".format(data))

print("Mean: {:.1f}".format(np.mean(data)))
print("Median: {:.1f}".format(np.median(data)))
print("Range: {:.0f}".format(np.max(data) - np.min(data)))
print("Quartile 1: {:.1f}".format(np.percentile(data, 25)))
print("Quartile 2: {:.1f}".format(np.percentile(data, 50)))
print("Quartile 3: {:.1f}".format(np.percentile(data, 75)))
print("Inter-Quartile Range: {:.1f}".format(np.percentile(data, 75) - np.percentile(data, 25)))
print("Variance: {:.1f}".format(np.var(data)))
print("Standard Deviation: {:.1f}".format(np.std(data)))
