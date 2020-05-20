#!/usr/bin/env python

import numpy as np

numTrails = 10_00_000
data = []

for n in range(numTrails):
    data.append(np.sum(np.random.randint(2, size=3)))

heads, counts = np.unique(data, return_counts=True)
print(heads, counts)
