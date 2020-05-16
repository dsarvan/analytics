#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = binom.rvs(n=5, p=0.5, size=3200)
heads, freq = np.unique(data, return_counts=True)

dframe = pd.DataFrame({'Heads':heads, 'Frequencies':freq})
print("Frequencies of distribution of heads: \n{}".format(dframe))

print("Mean: {:.3f}".format(data.mean()))
print("Standard Deviation: {:.3f}".format(data.std()))

plt.figure(dpi=120)
sns.distplot(data)
plt.xlabel("Random Variable")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.savefig("binormdistplot.pdf")
plt.show()
