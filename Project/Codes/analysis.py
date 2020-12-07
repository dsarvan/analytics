#!/usr/bin/env python3
# File: analysis.py
# Name: D.Saravanan
# Date: 07/12/2020
# Script to analyse financial data from NSE

import pandas as pd

# listed companies in NSE
nse = pd.read_csv('/home/saran/Analytics/Project/Data/MCAP_31032020_0.csv', index_col=0)
nse.index.name = None
