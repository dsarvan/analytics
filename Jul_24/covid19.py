#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

df = pd.read_csv('/home/saran/Analytics/Jul_11/time_series_covid19_confirmed_global.csv')
df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
df = df.groupby('Country/Region').sum()

df['Total'] = df.sum(axis=1)
df = df.sort_values(by=['Total'], ascending=False).head(5)
df = df.drop('Total', axis=1)

df = df.rename(columns={'US':'United States'})
df = df.T

plt.figure(); df.plot(kind='bar'); 
plt.savefig('plot.pdf'); plt.show()
