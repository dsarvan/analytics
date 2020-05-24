#!/usr/bin/env python3
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-x**2/2)

ans, err = quad(integrand, -1.85, -0.90)
print("The area under the standard normal curve P(-1.85 < Z < -0.90) is {:.5f}".format(ans))
