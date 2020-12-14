#!/usr/bin/env python3
# File: analysis.py
# Name: D.Saravanan
# Date: 07/12/2020
# Script to analyse financial data from NSE

from datetime import date
from nsepy import get_history
import numpy as np
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
data = data.loc[:, data.isnull().mean() < .01]

# price change
price = pd.DataFrame()
dt = 1
for name in data.columns:
    price[name] = [np.log(data[name][t+dt]) - np.log(data[name][t]) for t in range(len(data)-dt)]

print(price.describe())
#print(price['CIPLA'].skew())

# normalized return
#nprice = pd.DataFrame()
#for name in price.columns:
#    nprice[name] = [(price[name][t] - np.mean(price[name]))/np.std(price[name], ddof=1) for t in range(len(price))]

#print(nprice.describe())
#print(nprice['CIPLA'].skew())

#normalized = (price - price.min())/(price.max() - price.min())
#print(normalized.describe())
