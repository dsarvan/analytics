import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
randf = df.sample(n = 100)
fildf = randf.fillna(method = 'bfill')
findf = fildf.replace(to_replace = np.nan, value = 0)

print("Number of missing values of the cleaned sample dataset: {}".format(findf.isnull().sum().sum()))
