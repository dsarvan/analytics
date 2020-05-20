#!/usr/bin/env python3
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
plt.style.use('seaborn')

k_value = [0, 1, 2, 3, 4]
Frequency = [109, 65, 22, 3, 1]

N = np.sum(Frequency)
mu = np.sum(np.multiply(k_value, Frequency))/N

Calculated = []
for n in k_value:
    Calculated.append(N * (poisson.pmf(k=n, mu=mu, loc=0)))

ax = plt.figure().add_subplot(111)
ax.plot(k_value, Frequency, '--bo', label="Observed")
ax.plot(k_value, Calculated, '--ro', label="Expected")
ax.set(xlabel='k', ylabel='Frequency', title='Calculation of Poisson frequencies')
plt.legend(); plt.savefig('frequency.pdf')
