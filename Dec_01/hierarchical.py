#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

data = {'X': [0.40, 0.22, 0.35, 0.26, 0.08, 0.45], 'Y': [0.53, 0.38, 0.32, 0.19, 0.41, 0.30]}
df = pd.DataFrame(data, index = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'])
matrix = pd.DataFrame(distance_matrix(df.values, df.values), index = df.index, columns = df.index)

print(matrix)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.matshow(matrix, cmap='Reds')
xlabels = ["P%d" % i for i in range(7)]
ylabels = ["P%d" % i for i in range(7)]
ax.set_xticklabels(xlabels)
ax.set_yticklabels(ylabels)
fig.savefig('plot.pdf')
