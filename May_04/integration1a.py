#!/usr/bin/env python3
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-x**2/2)

ans, err = quad(integrand, 2.70, np.inf)
print("The area under the standard normal curve P(Z > 2.70) is {:.5f}".format(ans))
