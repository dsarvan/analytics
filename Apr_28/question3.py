import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
percent = (df.isnull().sum().sum() * 100)/(len(df.index)*len(df.columns))
print("Percentage of total missing values: {:.2f}".format(percent))
