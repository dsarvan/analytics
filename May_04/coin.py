#!/usr/bin/env python3
# File: coin.py
# Name: D.Saravanan
# Date: 04 May 2020
# Comment: Script to find Frequency Distribution and Probability
# Distribution of number of heads when a fair coin is tossed 6 times  

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

numTrails = 10_00_000
data = []

for n in range(numTrails):
    data.append(np.sum(np.random.randint(2, size=6)))
    
heads, counts = np.unique(data, return_counts=True)
df = pd.DataFrame({"Heads":heads, "Frequency":counts})
df["Probability"] = df["Frequency"]/numTrails

plt.figure(dpi=120)
sns.barplot(x="Heads", y="Frequency", data=df)
plt.title("Frequency Distribution Plot")
plt.savefig("freqdist.pdf")

plt.figure(dpi=120)
sns.barplot(x="Heads", y="Probability", data=df)
plt.title("Probability Distribution Plot")
plt.savefig("probdist.pdf")

plt.show()
