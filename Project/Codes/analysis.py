#!/usr/bin/env python3


import pandas_datareader.data as web
from datetime import datetime

data = web.DataReader('TCS', 'yahoo', start = '2014', end = datetime(2019, 5, 24))
print(data.head())
print(data.shape)
