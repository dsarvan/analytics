import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
brics = df.loc[df['country'].isin(['Brazil', 'China', 'India', 'South Africa'])]

india_lex = india['lifeExp'].mean()
india_pop = india['pop'].mean()
india_gdp = india['gdpPercap'].mean()

brics_lex = brics['lifeExp'].mean()
brics_pop = brics['pop'].mean()
brics_gdp = brics['gdpPercap'].mean()

print("'''BRICS 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(brics_lex))
print("Population: {:.0f}".format(brics_pop))
print("GDP per capita: {:.6f}".format(brics_gdp))

print("\n'''Difference between BRICS and India 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(brics_lex - india_lex))
print("Population: {:.0f}".format(brics_pop - india_pop))
print("GDP per capita: {:.6f}".format(brics_gdp - india_gdp))
