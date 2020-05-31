#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# create a dataframe by reading iris.csv
df = pd.read_csv("/home/saran/Analytics/May_27/iris.csv")

x = df.iloc[:,1:5].values
y = df.iloc[:,5].values

# x into standard normal variable
z = StandardScaler().fit_transform(x)

# compute mean of all columns
mean_vec = np.mean(z, axis=0)

# covariance matrix
cov_mat = (z - mean_vec).T.dot(z - mean_vec)/(x.shape[0] - 1)

# covariance matrix using numpy
#cov_mat = np.cov(z.T)

# eigen values and eigen vectors
eig_val, eig_vec = np.linalg.eig(cov_mat)

# eigen pairs
eig_pairs = [(np.abs(eig_val[i]),eig_vec[:,i]) for i in range(len(eig_val))]

# var exp
var_exp = [(i/sum(eig_val))*100 for i in sorted(eig_val, reverse=True)]

# cumulative var exp
cum_var_exp = np.cumsum(var_exp)

matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1), eig_pairs[1][1].reshape(4,1)))

projected_data = z.dot(matrix_w)
projected_data = pd.DataFrame(data=projected_data, columns=["PC1", "PC2"])

final_df = pd.concat((projected_data, df.iloc[:,5]), axis=1)
print(final_df)

ax1 = final_df.plot.scatter(x="PC1", y="PC2", c="red")
plt.show()
