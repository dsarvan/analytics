#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# compute cumulative distribution function (CDF)
# P(Z < -1.88)
x = -1.88; loc = 0; scale = 1
pls = norm.cdf(x, loc, scale)
print("The area under the standard normal curve P(Z < -1.88) is {:.5f}".format(pls))

x1=np.linspace(-10,x,1000);y1=norm.pdf(x1,loc,scale)
x2=np.linspace(-4,4,1000); y2=norm.pdf(x2,loc,scale)
ax = plt.figure().add_subplot(111);   ax.minorticks_on()
ax.plot(x2,y2,label='P(Z < -1.88) = {:.5f}'.format(pls))
ax.fill_between(x1,y1,0,alpha=0.5,color='b')
ax.fill_between(x2,y2,0,alpha=0.1,color='b')
ax.set(xlim=[-4,4], yticklabels=[]);   ax.legend(handlelength=0)
plt.savefig('norm1d.pdf',dpi=72,bbox_inches='tight'); plt.show()
