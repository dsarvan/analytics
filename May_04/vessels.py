#!/usr/bin/env python3
from scipy.stats import binom

# probability of success, p = 0.9 and number of observations, n = 5
# P(X >= 4)
pls = binom.sf(k=4, n=5, p=0.9, loc=1)
print("The probability of getting at least 4 success is {:.4f}".format(pls))

