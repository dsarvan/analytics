import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
bimstec = df.loc[df['country'].isin(['Bangladesh', 'India', 'Myanmar', 'Nepal', 'Sri Lanka', 'Thailand'])]

india_lex = india['lifeExp'].mean()
india_pop = india['pop'].mean()
india_gdp = india['gdpPercap'].mean()

bimstec_lex = bimstec['lifeExp'].mean()
bimstec_pop = bimstec['pop'].mean()
bimstec_gdp = bimstec['gdpPercap'].mean()

print("'''BIMSTEC 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(bimstec['lifeExp'].mean()))
print("Population: {:.0f}".format(bimstec['pop'].mean()))
print("GDP per capita: {:.6f}".format(bimstec['gdpPercap'].mean()))

print("\n'''Difference between BIMSTEC and India 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(bimstec_lex - india_lex))
print("Population: {:.0f}".format(bimstec_pop - india_pop))
print("GDP per capita: {:.6f}".format(bimstec_gdp - india_gdp))
