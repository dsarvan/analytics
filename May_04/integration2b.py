#!/usr/bin/env python3
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))

mu = 300; sigma = 25
ans, err = quad(integrand, 220, 260)
print("Probability, P(220 < X < 260): {:.5f}".format(ans))
print("Percentage,  P(220 < X < 260): {:.2f}".format(ans*100))
