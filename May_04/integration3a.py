#!/usr/bin/env python3
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))

mu = 120; sigma = 40
ans, err = quad(integrand, 150, np.inf)
print("Probability, P(X > 150): {:.5f}".format(ans))
