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
print("\nCritical values are {:.5f}, {:.5f}".format(zcritical_l, zcritical_u))

# decision making: z-statistic and critical values
if zstatistic < zcritical_l or zstatistic > zcritical_u:
    print("Reject the Null hypothesis.")
else: print("Fail to reject the Null hypothesis.")

# calculation of p-value:
zstatistic = -zstatistic if zstatistic > 0 else zstatistic
pvalue = 2*norm.cdf(zstatistic)
print("\np-value: {:.5f}".format(pvalue))

# decision making: p-value and level of significance
if pvalue < alpha: print("Reject the Null hypothesis.")
else: print("Fail to reject the Null hypothesis.")

# standard error
std_err = p_stdv/np.sqrt(n)
print("\nStandard Error: {:.5f}".format(std_err))

# confidence interval
cnf_int = s_mean + std_err * np.array([zcritical_l, zcritical_u])
print("Confidence Interval: {}".format(cnf_int))

x1=np.linspace(-10,zcritical_l,1000); y1=norm.pdf(x1)
x2=np.linspace(zcritical_u,10,1000);  y2=norm.pdf(x2)
x3=np.linspace(-4,4,1000); y3=norm.pdf(x3)
ax=plt.figure().add_subplot(111); ax.plot(x3,y3,color='brown')
ax.fill_between(x1,y1,0,alpha=0.5,color='brown',label='Rejection Region')
ax.fill_between(x2,y2,0,alpha=0.5,color='brown'); ax.set(xlabel='X',ylabel='P(X)')
ax.axvline(x=zstatistic,ls='--',c='b',label='z-statistic = {:.5f}'.format(zstatistic))
ax.set(xlim=[-4,4],title="z-distribution"); plt.legend(); plt.show()
