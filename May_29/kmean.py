#!/usr/bin/env python3
import numpy as np
import pandas as pd

# read csv file and create dataframe
df = pd.read_csv("objects.csv")

# randomly select rows of size = 2
dfs = df.sample(n=2, axis=0, replace=False)
df1 = dfs.iloc[0]; df2 = dfs.iloc[1]

D1=[sum([abs(df1.x-df.x[n]),abs(df1.y-df.y[n]),abs(df1.z-df.z[n])]) for n in range(len(df))]
D2=[sum([abs(df2.x-df.x[n]),abs(df2.y-df.y[n]),abs(df2.z-df.z[n])]) for n in range(len(df))]

# adding columns with values of D1 and D2 to dataframe
df['Distance from C1({},{},{})'.format(df1.x,df1.y,df1.z)] = D1
df['Distance from C2({},{},{})'.format(df2.x,df2.y,df2.z)] = D2

print(df)

cluster_1 = []
cluster_2 = []
for n in range(len(df)): 
    if D1[n] < D2[n]: cluster_1.append(df.iloc[n])
    else: cluster_2.append(df.iloc[n])

c1 = pd.DataFrame(cluster_1)
c2 = pd.DataFrame(cluster_2)

df1x = np.mean(c1.x); df1y = np.mean(c1.y); df1z = np.mean(c1.z)
df2x = np.mean(c2.x); df2y = np.mean(c2.y); df2z = np.mean(c2.z)

for n in range(len(c1)): print(c1['x'].iloc[n])

D3=[sum([abs(df1x-c1['x'].iloc[n]),abs(df1y-c1['y'].iloc[n]),abs(df1z-c1['z'].iloc[n])]) \
        for n in range(len(c1))]
D4=[sum([abs(df2x-c2['x'].iloc[n]),abs(df2y-c2['y'].iloc[n]),abs(df2z-c2['z'].iloc[n])]) \
        for n in range(len(c2))]

print(D3, D4)
