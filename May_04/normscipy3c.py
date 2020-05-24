#!/usr/bin/env python3
from scipy.stats import norm

# compute cumulative distribution function (CDF)
# P(60 < X < 90)
x=60; y=90; loc=120; scale=40
pls = norm.cdf(y,loc,scale) - norm.cdf(x,loc,scale)
print("Probability, P(60 < X < 90): {:.5f}".format(pls))
