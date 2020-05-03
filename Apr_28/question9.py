import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
randf = df.sample(n = 100)
fildf = randf.fillna(method = 'bfill')
findf = fildf.replace(to_replace = np.nan, value = 0)

print("Number of NA values before replacing with the next value: {}".format(randf.isnull().sum().sum()))
print("Number of NA values after replacing with the next value: {}".format(fildf.isnull().sum().sum()))
print("Number of missing values after replacing NA with value 0: {}".format(findf.isnull().sum().sum()))
