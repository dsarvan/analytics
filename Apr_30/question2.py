import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
india = india.set_index('year', drop = True)
india.index.name = None
india = india.loc[:, 'lifeExp':'gdpPercap']
india.columns = ['LifeExp', 'Population', 'GDPperCapita']
print(india)
