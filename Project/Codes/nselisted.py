#!/usr/bin/env python3

import pandas as pd

nse = pd.read_csv('/home/saran/Analytics/Project/Data/MCAP_31032020_0.csv', index_col=0)
nse.index.name = None



print(type(nse))
print(nse.head())
print(nse.tail())
