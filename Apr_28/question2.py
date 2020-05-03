import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
print(df.isnull().sum()*100/len(df))
