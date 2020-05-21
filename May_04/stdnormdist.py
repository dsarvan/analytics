#!/usr/bin/env python3
from scipy.stats import norm

# compute survival function (SF)
# P(Z >= 2.70)
pls = norm.sf(x=2.70, loc=0, scale=1)
print("The area under the standard normal curve which lie to the right of Z = 2.70 is {:.5f}".format(pls))

# compute cumulative distribution function (CDF)
# P(Z <= 1.73)
pms = norm.cdf(x=1.73, loc=0, scale=1)
print("The area under the standard normal curve which lie to the left of Z = 1.73 is {:.5f}".format(pms))

# compute survival function (SF)
# P(Z >= -0.66)
pls = norm.sf(x=-0.66, loc=0, scale=1)
print("The area under the standard normal curve which lie to the right of Z = -0.66 is {:.5f}".format(pls))

# compute cumulative distribution function (CDF)
# P(Z <= -1.88)
pms = norm.cdf(x=-1.88, loc=0, scale=1)
print("The area under the standard normal curve which lie to the left of Z = -1.88 is {:.5f}".format(pms))
