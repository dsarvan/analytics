import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']

print("'''India 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(india['lifeExp'].mean()))
print("Population: {:.0f}".format(india['pop'].mean()))
print("GDP per capita: {:.6f}".format(india['gdpPercap'].mean()))
