import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
india = india.set_index('year', drop = True)
india.index.name = None
india = india.loc[:, 'lifeExp':'gdpPercap']
india.columns = ['Life Exp', 'Population', 'GDPperCapita']
india = india.pct_change() * 100

ax = india.plot(figsize=(10, 10), subplots=True, kind="bar", grid=True, legend=False)
ax[0].set(ylabel='Life Expectancy Growth Rate', ylim=[0,10], title="India 1952-2007 Data")
ax[1].set(ylabel='Population Growth Rate', ylim=[0,15], title=" ")
ax[2].set(ylabel='GDP per capita Growth Rate', ylim=[0,50], title=" ")
ax[2].set_xlabel('Year')
plt.tight_layout()
plt.savefig('grate.png')
plt.show()
