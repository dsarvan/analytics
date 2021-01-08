#!/usr/bin/env python3
# File: program.py
# Name: D.Saravanan
# Date: 08/01/2020

import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

data = pd.read_csv('cdr.txt', sep=',')

data.columns = ['Caller_id', 'Calling_no', 'Called_no', 'Start_time', 'End_time', 'Type', 'Cost', 'Status']

vdata = data[data['Type'] == "VOICE"]
sdata = data[data['Type'] == "SMS"]

total_cost = data.groupby(['Calling_no', 'Called_no']).agg({'Cost': ['sum']}).reset_index()
vtotal_cost = vdata.groupby(['Calling_no', 'Called_no']).agg({'Cost': ['sum']}).reset_index()
stotal_cost = sdata.groupby(['Calling_no', 'Called_no']).agg({'Cost': ['sum']}).reset_index()

print(total_cost)
print(vtotal_cost)
print(stotal_cost)
