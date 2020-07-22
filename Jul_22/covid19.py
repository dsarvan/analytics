#!/usr/bin/env python3

import pandas as pd
import pandas_alive

df = pd.read_csv('time_series_covid19_confirmed_global.csv')
df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
df = df.groupby('Country/Region').sum()
df = df.T

#df = df.sum(axis=0)
#df = df.sort_values(ascending=False).head(25)

df = df[['US', 'Brazil', 'Russia', 'India', 'Spain', 'Italy', 'United Kingdom', 'France', \
        'Germany', 'Iran', 'Peru', 'Turkey', 'Chile', 'China', 'Mexico', 'Pakistan', \
        'Saudi Arabia', 'Canada', 'South Africa', 'Bangladesh', 'Belgium', 'Qatar', \
        'Colombia', 'Netherlands', 'Sweden']]

df.to_csv('covidata.csv', sep=',')
df = pd.read_csv('covidata.csv', index_col=0, parse_dates=[0], thousands=',')
df.plot_animated(filename='covid19.gif', period_fmt='%D')
