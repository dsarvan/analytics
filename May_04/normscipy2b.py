#!/usr/bin/env python3
from scipy.stats import norm

# compute cumulative distribution function (CDF)
# P(220 < X < 260)
x=220; y=260; loc=300; scale=25
pls = norm.cdf(y,loc,scale) - norm.cdf(x,loc,scale)
print("Probability, P(220 < X < 260): {:.5f}".format(pls))
print("Percentage,  P(220 < X < 260): {:.2f}".format(pls*100))
