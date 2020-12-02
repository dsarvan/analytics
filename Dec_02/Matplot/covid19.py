#!/usr/bin/env python3
# File: covid19.py
# Name: D.Saravanan
# Date: 02/12/2020
# Script to visualize Covid-19 confirmed cases by bar chart race with matplotlib

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

from urllib.request import urlretrieve

url = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/' 
       'master/csse_covid_19_data/csse_covid_19_time_series/' 
       'time_series_covid19_confirmed_global.csv')

urlretrieve(url, 'time_series_covid19_confirmed_global.csv')

data = pd.read_csv('time_series_covid19_confirmed_global.csv')
data = data.drop(['Province/State', 'Lat', 'Long'], axis=1)
data = data.groupby('Country/Region').sum()

#data['Total'] = data.sum(axis=1)
#data = data.sort_values(by='Total', ascending=False)
#data = data.drop(['Total'], axis=1)

data = data.T
data.rename(columns={'Holy See': 'Vatican', 'US': 'United States', 'West Bank and Gaza': 'Palestine'}, inplace=True)
data = data.drop(['Diamond Princess'], axis=1)

data.to_csv('covid19confirmed.csv', sep=',')
data = pd.read_csv('covid19confirmed.csv', index_col=0, parse_dates=[0], thousands=',')

#colors = dict(zip(['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burma','Burundi','Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo (Brazzaville)','Congo (Kinshasa)','Costa Rica','Cote d'Ivoire','Croatia','Cuba','Cyprus','Czechia','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Holy See','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Korea, South','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','MS Zaandam','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Namibia','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Macedonia','Norway','Oman','Pakistan','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Timor-Leste','Togo','Trinidad and Tobago','Tunisia','Turkey','US','Uganda','Ukraine','UAE','UK','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','West Bank and Gaza','Western Sahara','Yemen','Zambia','Zimbabwe'], ['#000000', ]  ))




#fig, ax = plt.subplots(111)
