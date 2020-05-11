#!/usr/bin/env python3
# File: poiss.py
# Name: D.Saravanan
# Date: 04 May 2020
# Comment: Poisson Distribution

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import poisson
sns.set()

data = poisson.rvs(mu=5.5, size=100)
print(np.unique(data, return_counts=True))

plt.figure(dpi=120)
sns.distplot(data)
plt.xlabel("Random Variable")
plt.ylabel("Probability")
plt.savefig("poisson.pdf")
plt.show()
