#!/usr/bin/env python3
# File: analysis.py
# Name: D.Saravanan
# Date: 07/12/2020
# Script to analyse financial data from NSE

from datetime import date
from nsepy import get_history
import pandas as pd

# listed companies in NSE
nse = pd.read_csv('/home/saran/Analytics/Project/Data/MCAP_31032020_0.csv', index_col=0)
nse.index.name = None

# historical stock price values
for name in nse['Symbol']:
    data = get_history(symbol = name, start = date(2010,1,1), end = date(2019,12,31))
    data.to_csv('data_{}.csv'.format(name))
