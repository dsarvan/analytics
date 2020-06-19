#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.stats import chi2

group = np.random.choice(a = ["G1", "G2", "G3", "G4", "G5"], p=[0.05, 0.15, 0.25, 0.05, 0.50], size=1000)
party = np.random.choice(a = ["P1", "P2", "P3"], p=[0.4, 0.2, 0.4], size=1000)

# create a data frame
df = pd.DataFrame({"group":group, "party":party})

# cross tabulation
df_tab = pd.crosstab(df.group, df.party, margins=True)

# create contingency table form given data frame
df_tab.index = ["G1", "G2", "G3", "G4", "G5", "col_total"]
df_tab.columns = ["P1", "P2", "P3", "row_total"]

print(df_tab)

observed = df_tab.iloc[0:5, 0:3]
expected = np.outer(df_tab["row_total"][0:5], df_tab.loc["col_total"][0:3])/1000
expected = pd.DataFrame(expected)
expected.columns = ["P1", "P2", "P3"]
expected.index = ["G1", "G2", "G3", "G4", "G5"]

chi_stat = (((observed - expected)**2)/expected).sum().sum()
chi_crit = chi2.ppf(0.95, 4)
p_value_ = 1 - chi2.cdf(chi_stat, 4)

print(chi_stat, chi_crit, p_value_)
