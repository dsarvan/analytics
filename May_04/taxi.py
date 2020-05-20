#!/usr/bin/env python3
from scipy.stats import poisson

# compute probability mass function (PMF)
# P(X = 0)
pes = poisson.pmf(k=0, mu=3, loc=0)
print("The probability that no accidents in a year: {:.4f}".format(pes))

# compute survival function (SF)
# P(X > 3)
pgs = poisson.sf(k=3, mu=3, loc=0)
print("The probability that more than 3 accidents in a year: {:.4f}".format(pgs))
