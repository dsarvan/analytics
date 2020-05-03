import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
saarc = df.loc[df['country'].isin(['Afghanistan', 'Bangladesh', 'India', 'Nepal', 'Pakistan', 'Sri Lanka'])]

india_lex = india['lifeExp'].mean()
india_pop = india['pop'].mean()
india_gdp = india['gdpPercap'].mean()

saarc_lex = saarc['lifeExp'].mean()
saarc_pop = saarc['pop'].mean()
saarc_gdp = saarc['gdpPercap'].mean()

print("'''SAARC 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(saarc['lifeExp'].mean()))
print("Population: {:.0f}".format(saarc['pop'].mean()))
print("GDP per capita: {:.6f}".format(saarc['gdpPercap'].mean()))

print("\n'''Difference between SAARC and India 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(saarc_lex - india_lex))
print("Population: {:.0f}".format(saarc_pop - india_pop))
print("GDP per capita: {:.6f}".format(saarc_gdp - india_gdp))
