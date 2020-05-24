#!/usr/bin/env python3
from scipy.stats import norm

# compute survival function (SF)
# P(X > 350)
pls = norm.sf(x=350, loc=300, scale=25)
print("Probability, P(X > 350): {:.5f}".format(pls))
