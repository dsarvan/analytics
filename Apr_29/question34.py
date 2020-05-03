import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
g4 = df.loc[df['country'].isin(['Brazil', 'Germany', 'India', 'Japan'])]

india_lex = india['lifeExp'].mean()
india_pop = india['pop'].mean()
india_gdp = india['gdpPercap'].mean()

g4_lex = g4['lifeExp'].mean()
g4_pop = g4['pop'].mean()
g4_gdp = g4['gdpPercap'].mean()

print("'''G4 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(g4['lifeExp'].mean()))
print("Population: {:.0f}".format(g4['pop'].mean()))
print("GDP per capita: {:.6f}".format(g4['gdpPercap'].mean()))

print("\n'''Difference between G4 and India 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(g4_lex - india_lex))
print("Population: {:.0f}".format(g4_pop - india_pop))
print("GDP per capita: {:.6f}".format(g4_gdp - india_gdp))
