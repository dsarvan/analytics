#!/usr/bin/env python3
# File: analysis.py
# Name: D.Saravanan
# Date: 07/12/2020
# Script to analyse financial data from NSE

from datetime import date
from nsepy import get_history
import numpy as np
import scipy.linalg as la
import pandas as pd

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

## listed companies in NSE
#nse = pd.read_csv('/home/saran/Analytics/Project/Data/MCAP_31032020_0.csv', index_col=0)
#nse.index.name = None
#
## historical stock price values
#for name in nse['Symbol']:
#    data = get_history(symbol = name, start = date(2010,1,1), end = date(2019,12,31))
#    data.to_csv('data_{}.csv'.format(name))
#
## close stock price values
#close = pd.DataFrame()
#for name in nse['Symbol']:
#    data = pd.read_csv('Dataset/data_{}.csv'.format(name), usecols=['Date','Close'])
#    close[['Date', name]] = data[['Date', 'Close']]
#    close.to_csv('closeprice.csv', index=False)

data = pd.read_csv('closeprice.csv', index_col=0)
data.index.name = None

# remove columns with number of NaN greater than 1%
data = data.loc[:, data.isnull().mean() < .003]

# price change
price = pd.DataFrame()
dt = 1
for name in data.columns:
    price[name] = [np.log(data[name][t+dt]) - np.log(data[name][t]) for t in range(len(data)-dt)]

# normalized return
nprice = pd.DataFrame()
for name in price.columns:
    nprice[name] = [(price[name][t] - np.mean(price[name]))/np.std(price[name], ddof=1) for t in range(len(price))]

# correlation matrix
C = nprice.corr()

# eigenvalues and eigenvectors calculation for elements in correlation matrix
values, vectors = la.eig(C.to_numpy())

print(min(values))
print(max(values))

# T is the number of dates for which data was collected and N is the number of stocks being studied
# T x N random matrix with elements that belong to a standard normal distribution having mean 0 and variance 1
columns = [f'column_{num}' for num in range(nprice.shape[1])]
index = [f'index_{num}' for num in range(nprice.shape[0])]
A = pd.DataFrame(np.random.normal(loc = 0, scale = 1, size = nprice.shape), columns = columns, index = index)
#A = pd.DataFrame(np.random.randn(nprice.shape[0], nprice.shape[1]), columns = columns, index = index)

# N x N random matrix whose elements are all uncorrelated
R = A.corr()

# eigenvalues and eigenvectors calculation for elements in random matrix
rvalues, rvectors = la.eig(R.to_numpy())

print(min(rvalues))
print(max(rvalues))
