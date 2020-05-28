#!/usr/bin/env python3
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

def similar_variance(n1,s1_mean,n2,s2_mean):
    dof = n1+n2-2
    sp = np.sqrt(((n1-1)*s1_stdv**2+(n2-1)*s2_stdv**2)/(dof))
    return (s1_mean-s2_mean)/(sp * np.sqrt(1/n1 + 1/n2)), dof, sp

def non_similar_variance(n1,s1_mean,n2,s2_mean):
    sd = np.sqrt(s1_stdv**2/n1 + s2_stdv**2/n2)
    dof = (sd**4)/(((s1_std**2/n1)**2/(n1-1)) + ((s2_std**2/n2)**2/(n2-1)))
    return (s1_mean-s2_mean)/sd, dof, sd

def ttest_and_variance(s1_stdv, s2_stdv):
    if 0.5 < s1_stdv/s2_stdv < 2:
        return similar_variance(n1,s1_mean,n2,s2_mean)
    else:
        return non_similar_variance(n1,s1_mean,n2,s2_mean)

print("__________Two-sample T-test for unpaired data__________\n")

sample1 = [float(value) for value in input("Sample_1 values: ").split()]
sample2 = [float(value) for value in input("Sample_2 values: ").split()]

# Number of Observations
n1 = len(sample1); n2 = len(sample2)

# Mean and Standard Deviation
s1_mean = np.mean(sample1); s1_stdv = np.std(sample1, ddof=1)
s2_mean = np.mean(sample2); s2_stdv = np.std(sample2, ddof=1)

# level of significance, confidence level
los = 0.05; cnl = 1 - los

# standard error (SE) of mean of sample1
std_err1 = s1_stdv/np.sqrt(n1)

print("\nSample 1: \n\t Number of Observations = {} \n\t Mean = {:.5f}".format(n1,s1_mean))
print("\t Standard Deviation = {:.5f}".format(s1_stdv))
print("\t Standard Error of the Mean = {:.5f}".format(std_err1))

# standard error (SE) of mean of sample2
std_err2 = s2_stdv/np.sqrt(n2)

print("\nSample 2: \n\t Number of Observations = {} \n\t Mean = {:.5f}".format(n2,s2_mean))
print("\t Standard Deviation = {:.5f}".format(s2_stdv))
print("\t Standard Error of the Mean = {:.5f}".format(std_err2))

# calculation of T-statistics and degrees of freedom
tstatistics, dof, sp = ttest_and_variance(s1_stdv, s2_stdv)
print("\nT statistics: {:.5f}".format(tstatistics))

# calculation of Critical values
tcritical_l = t.ppf(q = los/2, df = dof)
tcritical_u = -tcritical_l
print("\nCritical values are {:.5f}, {:.5f}".format(tcritical_l, tcritical_u))

# decision making - using T-statistics and Critical values
if tstatistics < tcritical_l or tstatistics > tcritical_u:
    print("Reject the Null hypothesis.")
else: print("Fail to reject the Null hypothesis.")

# calculation of p-value
pvalue = 2*t.cdf(tstatistics, df = dof)
print("\np-value: {:.5f}".format(pvalue))

# decision making - using p-value and level of significance
if pvalue < los: print("Reject the Null hypothesis.")
else: print("Fail to reject the Null hypothesis.")

# standard error
std_error = sp * np.sqrt(1/n1 + 1/n2)
print("\nStandard Error: {:.5f}".format(std_error))

# confidence interval
cnf_int = (s1_mean - s2_mean) + std_error * np.array([tcritical_l, tcritical_u])
print("Confidence Interval: {}".format(cnf_int))

# plot script
x1=np.linspace(-10,tcritical_l,1000); y1=t.pdf(x1,df=dof)
x2=np.linspace(tcritical_u,10,1000);  y2=t.pdf(x2,df=dof)
x3=np.linspace(-4,4,1000); y3=t.pdf(x3,df=dof)
ax=plt.figure().add_subplot(111); ax.plot(x3,y3,color='brown')
ax.fill_between(x1,y1,0,alpha=0.5,color='brown',label='Rejection Region')
ax.fill_between(x2,y2,0,alpha=0.5,color='brown'); ax.set(xlabel='X',ylabel='P(X)')
ax.axvline(x=tstatistics,ls='--',c='b',label='T statistics = {:.5f}'.format(tstatistics))
ax.set(xlim=[-4,4],title="T Distribution (degrees of freedom = {:.0f})".format(dof))
plt.legend(); plt.savefig('tscript3.pdf',dpi=72,bbox_inches='tight'); plt.show()
