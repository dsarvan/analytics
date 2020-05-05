#!/usr/bin/env python3
# File: iris.py
# Name: D.Saravanan    Date: 19/03/2020
# Python script to plot iris dataset using seaborn

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")

sns.pairplot(df,hue='species')
plt.show()
