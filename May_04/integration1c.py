#!/usr/bin/env python3
import numpy as np
from scipy.integrate import quad

def integrand(x): return 1/np.sqrt(2*np.pi) * np.exp(-x**2/2)

ans, err = quad(integrand, -0.66, np.inf)
print("Area under the standard normal curve P(Z > -0.66): {:.5f}".format(ans))
