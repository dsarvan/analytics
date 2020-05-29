#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# compute cumulative distribution function (CDF): P(Z < 1.73)
x = 1.73; loc = 0; scale = 1
pls = norm.cdf(x, loc, scale)
print("Area under the standard normal curve P(Z < 1.73): {:.5f}".format(pls))

x1=np.linspace(-10,x,1000);y1=norm.pdf(x1,loc,scale)
x2=np.linspace(-4,4,1000); y2=norm.pdf(x2,loc,scale)
ax = plt.figure().add_subplot(111); ax.minorticks_on()
ax.plot(x2,y2,c='r',label='P(Z < 1.73) = {:.5f}'.format(pls))
ax.set(xlabel='X',ylabel='P(X)'); ax.legend(handlelength=0)
ax.fill_between(x1,y1,alpha=0.5,color='r'); ax.set(xlim=[-4,4])
plt.savefig('norm1b.pdf',dpi=72,bbox_inches='tight'); plt.show()
