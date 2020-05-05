#!/usr/bin/env python3
# File: dfclean.py
# Name: D.Saravanan    Date: 19/03/2020
# Python script for dataframe cleaning with example.csv

import numpy as np
import pandas as pd

df = pd.read_csv('example.csv')
print(df)
df_mean = df.groupby('Country')['Age'].mean().reset_index()
df_mean.columns = ['Country','Age_mean']
df = pd.merge(df, df_mean, on='Country', how='inner')
df.loc[df['Age'].isnull(), 'Age'] = df['Age_mean']
df.drop('Age_mean',axis=1,inplace=True)
print(df)
