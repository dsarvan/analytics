#!/usr/bin/env python3
from scipy.stats import chisquare

Obs = [20,20,25,35]
Exp = [25,25,25,25]

chistat, pvalue = chisquare(f_obs = Obs, f_exp = Exp)
print("Chi-Square Statistics: ", chistat)
print("p-value: ", pvalue)
