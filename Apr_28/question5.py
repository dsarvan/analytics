import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
cdf = df.dropna(axis=1)
print("The total number of columns after dropping: {}".format(len(cdf.columns)))
print("The percentage of columns lost due to this operation: {:.1f}".format((len(df.columns)-len(cdf.columns))*100/len(df.columns)))
