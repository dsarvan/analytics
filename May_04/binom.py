#!/usr/bin/env python3
# File: binom.py
# Name: D.Saravanan
# Date: 04 May 2020
# comment: Binomial Distribution

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom
sns.set()

data = binom.rvs(n=6, p=0.5, size=100)

plt.figure(dpi=120)
sns.distplot(data)
plt.xlabel("Random Variable")
plt.ylabel("Probability")
plt.savefig("binomial.pdf")
plt.show()
