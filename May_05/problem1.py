#!/usr/bin/env python3

import numpy as np
from scipy.stats import chi2

Obs = np.array([20,20,25,35])
Exp = np.array([25,25,25,25])

chistatistics = np.sum((Obs-Exp)**2/Exp)
print("The Chi-Statistics is ", chistatistics)

# Critical value
chicritical = chi2.ppf(1-0.05, 3)
print("The Chi-Squared critical value is ", chicritical)

# Hypothesis-Testing
if chistatistics > chicritical:
    print("Hypothesis is rejected.")
else:
    print("Hypothesis is accepted.")
