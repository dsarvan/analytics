#!/usr/bin/env python3
import numpy as np
import pandas as pd

# read csv file and create dataframe
df = pd.read_csv("objects.csv")

# randomly select rows of size = 2
dfs = df.sample(n=2, axis=0, replace=False)
df1 = dfs.iloc[0]; df2 = dfs.iloc[1]

df1x = df1.x; df1y = df1.y; df1z = df1.z
df2x = df2.x; df2y = df2.y; df2z = df2.z

print("random 1 values: x:{} y:{} z:{}".format(df1x,df1y,df1z))
print("random 2 values: x:{} y:{} z:{}".format(df2x,df2y,df2z))

m = 0
while m < 4:

    D1=[sum([abs(df1x-df.x[n]),abs(df1y-df.y[n]),abs(df1z-df.z[n])]) for n in range(len(df))]
    D2=[sum([abs(df2x-df.x[n]),abs(df2y-df.y[n]),abs(df2z-df.z[n])]) for n in range(len(df))]

    # adding columns with values of D1 and D2 to dataframe
    df['Dist. from C1({:.1f},{:.1f},{:.1f})'.format(df1x,df1y,df1z)] = D1
    df['Dist. from C2({:.1f},{:.1f},{:.1f})'.format(df2x,df2y,df2z)] = D2

    print("\nk-mean cluster: \n{}".format(df))
    df = df[["Objects", "x", "y", "z"]]

    cluster_1 = []
    cluster_2 = []
    for n in range(len(df)): 
        if D1[n] < D2[n]: cluster_1.append(df.iloc[n])
        else: cluster_2.append(df.iloc[n])

    c1 = pd.DataFrame(cluster_1)
    c2 = pd.DataFrame(cluster_2)

    print("\nCluster 1: \n{}".format(c1))
    df1x = np.mean(c1.x); df1y = np.mean(c1.y); df1z = np.mean(c1.z)
    print("\nCluster 1: x_mean = {:.1f}, y_mean = {:.1f}, z_mean = {:.1f}".format(df1x, df1y, df1z))

    print("\nCluster 2: \n{}".format(c2))
    df2x = np.mean(c2.x); df2y = np.mean(c2.y); df2z = np.mean(c2.z)
    print("\nCluster 2: x_mean = {:.1f}, y_mean = {:.1f}, z_mean = {:.1f}".format(df2x, df2y, df2z))

    print("----------------------------------------------------------------------------------------")

    m = m + 1
