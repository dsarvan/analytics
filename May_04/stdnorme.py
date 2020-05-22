#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
plt.style.use('seaborn')

mu = 0; sigma = 1
x1 = np.linspace(-1.85,-0.90,1000)
x2 = np.linspace(mu-4*sigma,mu+4*sigma,1000)
y1 = norm.pdf(x1,mu,sigma)
y2 = norm.pdf(x2,mu,sigma)

ax = plt.figure().add_subplot(111)
ax.plot(x2,y2) # x and y axis values
ax.fill_between(x1,y1,0,alpha=0.5, color='b')
ax.fill_between(x2,y2,0,alpha=0.1, color='b')
ax.set(xlim=[-4,4], yticklabels=[])
plt.savefig('norm1e.pdf', dpi=72, bbox_inches='tight') 
plt.show()
