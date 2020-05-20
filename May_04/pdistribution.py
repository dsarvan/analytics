#!/usr/bin/env python3
from scipy.stats import poisson

# compute cumulative distribution function (CDF)
# P(X <= 5)
pms = poisson.cdf(k=5, mu=4, loc=0)
print("The probability that at most 5 defective fuses: {:.4f}".format(pms))
