#!/usr/bin/env python3
import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()

N = int(input("Enter the number of countries to display: "))
w = input("Enter Y to display the top {} countries based on GDP: ".format(N))

if w == 'Y':
	meandf = df.groupby('country')['gdpPercap'].mean()
	sortdf = meandf.sort_values(ascending=False).head(N)
	resetdf = sortdf.reset_index()

	print("\n'''Growth Percentage of top {} countries (1952-2007) Data'''".format(N))
	for name in resetdf['country']:
		country = df.loc[df['country'] == name]
		country = country.set_index('year', drop = True)
		country.index.name = None
		country = country.loc[:, 'lifeExp':'gdpPercap']
		country.columns = ['Life Exp', 'Population', 'GDPperCapita']
		country = country.pct_change()*100
		print("\n{}'s Growth Percentage Information \n {}".format(name, country))
