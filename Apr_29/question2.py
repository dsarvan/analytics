import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
print("'''World 1952-2007 Data'''")
print("Life Expectancy: {:.3f}".format(df['lifeExp'].mean()))
print("Population: {:.0f}".format(df['pop'].mean()))
print("GDP per capita: {:.6f}".format(df['gdpPercap'].mean()))
