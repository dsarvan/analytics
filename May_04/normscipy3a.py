#!/usr/bin/env python3
from scipy.stats import norm

# compute survival function (SF)
# P(X > 150)
pls = norm.sf(x=150, loc=120, scale=40)
print("Probability, P(X > 150): {:.5f}".format(pls))
