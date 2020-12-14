#!/usr/bin/env python3

import numpy as np
import pandas as pd
from datetime import date
from nsepy import get_history

#nse = pd.read_csv('/home/saran/Analytics/Project/Data/MCAP_31032020_0.csv', index_col=0)
#nse.index.name = None

#for name in nse['Symbol']:
#    data = get_history(symbol = name, start = date(2010,1,1), end = date(2019,12,31))
#    data.to_csv('data_{}.csv'.format(name))






data = pd.read_csv('/home/saran/Analytics/Project/Codes/ddfile.csv', index_col=0)
data.index.name = None

dprice = pd.DataFrame()

dt = 1
for name in data.columns:
    price = [np.log(data[name][t+dt]) - np.log(data[name][t]) for t in range(len(data)-dt)]
    dprice[name] = price

print(dprice)
















#cormat = data.corr()
#print(cormat)
