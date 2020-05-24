#!/usr/bin/env python3
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

sample = np.array([1,2,3,4,5])
p_mean = 3.5                      # populuation mean
s_mean = np.mean(sample)          # sample mean
s_stdv = np.std(sample, ddof=1)   # sample standard deviation

n = len(sample)                   # sample length
dof = n - 1                       # degrees of freedom
los = 0.05                        # level of significance
cnl = 1 - los                     # confidence level

print("Population Mean: {:.1f}".format(p_mean))
print("Number of samples: {}".format(n))
print("Sample Mean: {:.1f}".format(s_mean))
print("Sample Standard Deviation: {:.1f}".format(s_stdv))
print("Degree of freedom: {}".format(dof))
print("Confidence level: {:.2f}".format(cnl))
print("Significant level: {:.2f}".format(los))

tstatistics = (s_mean - p_mean)/(s_stdv/np.sqrt(n))
print("T statistics: {:.5f}".format(tstatistics))

tcritical_l = t.ppf(q = los/2, df = dof)
tcritical_u = -tcritical_l
print("Critical values are {}, {}".format(tcritical_l, tcritical_u))

# decision making - using statistics and critical value
if tstatistics < tcritical_l or tstatistics > tcritical_u:
    print("Reject the H0 Null hypothesis.")
else: print("Fail to reject the H0 Null hypothesis.")

# decision making - using p-value
pvalue = 2*t.cdf(tstatistics, df = dof)
print("p-value: {:.5f}".format(pvalue))
if pvalue < 0.05: print("Reject the H0 Null hypothesis.")
else: print("Fail to reject the H0 Null hypothesis.")

# standard error
std_error = s_stdv/np.sqrt(n)
print("Standard Error: {:.5f}".format(std_error))

# confidence interval
cint = s_mean + std_error * np.array([tcritical_l, tcritical_u])
print("Confidence Interval: {}".format(cint))

x1=np.linspace(-10,tcritical_l,1000); y1=t.pdf(x1,df=dof)
x2=np.linspace(tcritical_u,10,1000);  y2=t.pdf(x2,df=dof)
x3=np.linspace(-4,4,1000); y3=t.pdf(x3,df=dof)
ax=plt.figure().add_subplot(111); ax.plot(x3,y3,color='brown')
ax.fill_between(x1,y1,0,alpha=0.5,color='brown',label='Rejection Region')
ax.fill_between(x2,y2,0,alpha=0.5,color='brown'); ax.set(xlabel='X', ylabel='P(X)')
ax.axvline(x=tstatistics,ls='--',c='b',label='T statistics = {:.5f}'.format(tstatistics))
ax.set(xlim=[-4,4], title="T Distribution (degree of freedom = 4)"); plt.legend()
plt.savefig('ttest.pdf',dpi=72,bbox_inches='tight'); plt.show()
