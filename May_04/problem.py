#!/usr/bin/env python3

import numpy as np
from statistics import mode

population = np.random.randint(low=1, high=100, size=1_00_000)
print("Population: {}".format(population))
print("Length of Population: {}".format(len(population)))

sample = np.random.choice(population, size=20)
print("Sample: {}".format(sample))
print("Length of Sample: {}".format(len(sample)))

pmean = np.mean(population)
print("Mean of Population: {}".format(pmean))
smean = np.mean(sample)
print("Mean of Sample: {}".format(smean))

pmedian = np.median(population)
print("Median of Population: {}".format(pmedian))
smedian = np.median(sample)
print("Median of Sample: {}".format(smedian))

#pmode = mode(population)
#print("Mode of Population: {}".format(pmode))
#smode = mode(sample)
#print("Mode of Sample: {}".format(smode))

prange = np.max(population) - np.min(population)
print("Range of Population: {}".format(prange))
srange = np.max(sample) - np.min(sample)
print("Range of Sample: {}".format(srange))

pq1 = np.percentile(population, 25)
pq2 = np.percentile(population, 50)
pq3 = np.percentile(population, 75)
print("First Quartile of Population: {}".format(pq1))
print("Second Quartile of Population: {}".format(pq2))
print("Third Quartile of Population: {}".format(pq3))

sq1 = np.percentile(sample, 25)
sq2 = np.percentile(sample, 50)
sq3 = np.percentile(sample, 75)
print("First Quartile of Sample: {}".format(sq1))
print("Second Quartile of Sample: {}".format(sq2))
print("Third Quartile of Sample: {}".format(sq3))

piqr = pq3 - pq1
print("Inter-quartile Range of Population: {}".format(piqr))
siqr = sq3 - sq1
print("Inter-quartile Range of Sample: {}".format(siqr))

pvar = np.var(population)
print("Variance of Population: {}".format(pvar))
svar = np.var(sample)
print("Variance of Sample: {}".format(svar))

pstd = np.std(population)
print("Standard Deviation of Population: {}".format(pstd))
sstd = np.std(sample)
print("Standard Deviation of Sample: {}".format(sstd))
