#!/usr/bin/env python3
from scipy.stats import norm

# compute cumulative distribution function (CDF)
# P(100 < X < 150)
x=100; y=150; loc=120; scale=40
pls = norm.cdf(y,loc,scale) - norm.cdf(x,loc,scale)
print("Probability, P(100 < X < 150): {:.5f}".format(pls))
