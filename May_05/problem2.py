#!/usr/bin/env python3

import numpy as np
from scipy.stats import chi2
from scipy.stats import chisquare

Obs = np.array([50,45,5])
Exp = np.array([30,60,10])

chistatistics = np.sum((Obs-Exp)**2/Exp)
print("The Chi-Statistics is ", chistatistics)

# Calculation using chisquare
chistat, pvalue = chisquare(f_obs = Obs, f_exp = Exp)
print("Chi-Square statistics: ", chistat)
print("p-value: ", pvalue)

# Critical value
chicritical = chi2.ppf(0.05, 2)
print("The Chi-Squared critical value is ", chicritical)

# Hypothesis-Testing
if chistatistics > chicritical:
    print("Hypothesis is rejected.")
else:
    print("Hypothesis is accepted.")

