#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.stats import chi2

# read csv file as pandas dataframe
df = pd.read_csv("census.csv")

# replace 'Nan' with '288'
#df = df.replace('Nan', '288', regrex=True)
df = df.replace('Nan', '288')

# convert string to int
df['Hours Perweek'] = df['Hours Perweek'].astype(int)

# calculate median value where df['Hours Perweek'] < 100
median = df.loc[df['Hours Perweek'] < 100, 'Hours Perweek'].median()

# replace with median where df['Hours Perweek'] > 100
df['Hours Perweek'] = np.where(df['Hours Perweek'] > 100, median, df['Hours Perweek'])

print(df)
