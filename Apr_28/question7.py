import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
randf = df.sample(n = 100)
print("Number of (rows, columns): {}".format(randf.shape))
