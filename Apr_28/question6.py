import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
for name in df.columns: print(name)
