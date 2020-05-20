#!/usr/bin/env python3
from scipy.stats import binom

# compute survival function (SF)
# P(X >= 3)
pls = binom.sf(k=3, n=5, p=0.3, loc=1)
print("The probability of getting at least 3 success: {:.4f}".format(pls))

# compute cumulative distribution function (CDF)
# P(X <= 3)
pms = binom.cdf(k=3, n=5, p=0.3, loc=0)
print("The probability of getting at most 3 success: {:.4f}".format(pms))

# compute probability mass function (PMF)
# P(X = 2)
pef = binom.pmf(k=2, n=5, p=0.3, loc=0)
print("The probability of getting exactly 3 failure: {:.4f}".format(pef))
