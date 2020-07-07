#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

df = pd.DataFrame([[129,171], [31,69]])

Obs = df.values
total = np.sum(df.sum(axis=0))
nrows,ncols = df.shape

Exp = np.zeros(shape = (nrows,ncols))

for i in range(nrows):
    for j in range(ncols):
        rtotal = df.iloc[i,:].sum()
        ctotal = df.iloc[:,j].sum()
        Exp[i,j] = (rtotal*ctotal)/total

"""calculation of Chi-Statistics"""
chistatistics = np.sum((Obs-Exp)**2/Exp)
print("The Chi-Statistics is ", chistatistics)

"""degree of freedom"""
dof = (nrows - 1)*(ncols - 1)
print("Degree of freedom is ", dof)
