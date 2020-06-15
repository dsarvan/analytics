#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

print("__________z-test__________")

p_mean = float(input("\nPopulation mean: "))
p_stdv = float(input("Population stand_dev: "))
s_mean = float(input("Sample mean: "))
n = float(input("Sample length: "))
alpha = float(input("Level of significance: "))

# calculation of z-statistic
zstatistic = (s_mean - p_mean)/(p_stdv/np.sqrt(n))
print("\nz-statistic: {:.5f}".format(zstatistic))

# calculation of critical values
zcritical_l = norm.ppf(q = alpha/2)
zcritical_u = -zcritical_l 
#print("\nCritical values are {:.5f}, {:.5f}".format(zcritical_l, zcritical_u))

# standard error
std_err = p_stdv/np.sqrt(n)
print("\nStandard Error: {:.5f}".format(std_err))

# confidence interval
cnf_int = s_mean + std_err * np.array([zcritical_l, zcritical_u])
print("Confidence Interval: {}".format(cnf_int))
