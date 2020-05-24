#!/usr/bin/env python3
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))

mu = 120; sigma = 40
ans, err = quad(integrand, 60, 90)
print("Probability, P(60 < X < 90): {:.5f}".format(ans))
