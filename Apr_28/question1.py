import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
print("The total missing values in the dataset: {}".format(df.isnull().sum().sum()))
