#!/usr/bin/env python3

import numpy as np
import pandas as pd

df = pd.DataFrame([[7,9,24], [129,46,215]])

Obs = df.values
total = np.sum(df.sum(axis=0))
nrows,ncols = df.shape

Exp = np.zeros(shape = (nrows,ncols))

for i in range(nrows):
    for j in range(ncols):
        rtotal = df.iloc[i,:].sum()
        ctotal = df.iloc[:,j].sum()
        Exp[i,j] = (rtotal*ctotal)/total

print(Obs)
print(Exp)

chistatistics = np.sum((Obs-Exp)**2/Exp)
print("The Chi-Statistics is ", chistatistics)
