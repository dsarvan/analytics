#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-dark')

def init():
    ax.clear()
    #axes_style(ax)
    ax.set_ylim(.2, 6.8)

#def axes_style(ax):
#    ax.set_facecolor('.8')
#    ax.tick_params(labelsize=8, length=0)
#    ax.grid(True, axis='x', color='white')
#    ax.set_axisbelow(True)
#    [spine.set_visible(False) for spine in ax.spines.values()]

def data(df, steps=5):
    df = df.reset_index()
    df.index = df.index * steps
    lindex = df.index[-1] + 1
    df_ext = df.reindex(range(lindex))
    df_ext['Date'] = df_ext['Date'].fillna(method='ffill')
    df_ext = df_ext.set_index('Date')
    df_rext = df_ext.rank(axis=1, method='first')
    df_ext = df_ext.interpolate()
    df_rext = df_rext.interpolate()
    return df_ext, df_rext

df = pd.read_csv('time_series_covid19_confirmed_global.csv')
df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
df = df.groupby('Country/Region').sum()

df['Total'] = df.sum(axis=1)
df = df.sort_values(by=['Total'], ascending=False).head(5)
df = df.drop(['Total'], axis=1)
df = df.T
df.index.name = 'Date'; df.columns.name = ''
df_ext, df_rext = data(df)


colors = ['blue', 'green', 'white', 'orange', 'red']
labels = df_ext.columns

def update(i):
    for bar in ax.containers:
        bar.remove()

    y = df_rext.iloc[i]
    width = df_ext.iloc[i]
    ax.barh(y=y, width=width, color=colors, tick_label=labels)
    #date_str = df_ext.index[i].strftime('%B %-d, %Y')
    #ax.set_title(f'COVID-19 Confirmed Cases by Country - {date_str}', fontsize='smaller')

fig = plt.figure(figsize=(4, 2.5), dpi=144)
ax = fig.add_subplot()
anim = FuncAnimation(fig=fig, func=update, init_func=init, frames=len(df_ext), interval=100, repeat=False)
anim.save('covid19confirmed.gif')
