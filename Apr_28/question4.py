import numpy as np
import pandas as pd

df = pd.read_csv("DataSet/Building_Permits.csv")
rdf = df.dropna(axis=0)
print("The total number of rows after dropping: {}".format(len(rdf.index)))
print("The percentage of rows lost due to this operation: {:.1f}".format((len(df.index)-len(rdf.index))*100/len(df.index)))
