#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

df = pd.read_csv('/home/saran/Analytics/Jul_11/time_series_covid19_confirmed_global.csv')
df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
df = df.groupby('Country/Region').sum()
df = df.T
df = df.rename(columns={'US':'United States'})

#x = df.index.values
#y = df.columns.values

#num = 0

#for name in df.columns.values:
#    name = []
#    num += 1
#
#    for row in df.itertuples():
#        name.append(row[num])
#        print(name)

for date in df.index.values:
    plt.bar(date, df['India'])

plt.show()




#for date, value in df.iterrows():
    #for val in value:
    #    if val != 0: print(val)



    #print(index, row[value])
    #if value <= length:
    #    value += 1
    

#x = np.arange(len(x1))
#width = 0.35
#
#fig, ax = plt.subplots()
#rects = ax.bar(x - width/2, x1, width, label='Date')
#
#def autolabel(rects):
#    for rect in rects:
#        height = rect.get_height()
#        ax.annotate('{}'.format(height),
#                    xy=(rect.get_x() + rect.get_width() / 2, height),
#                    xytext=(0, 3), 
#                    textcoords="offset points",
#                    ha='center', va='bottom')
#
#autolabel(rects)
#
#fig.tight_layout()
#
#plt.show()

#plt.figure()
#for value in df['India']:
#    if value != 0:
#        plt.figure();
#        df['India'].plot(kind='barh', x=df.index.values, y=df.India) 
#        plt.savefig('plot.pdf'); plt.show()
