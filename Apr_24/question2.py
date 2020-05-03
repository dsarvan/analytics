import pandas as pd
N = input("Enter numbers: ").split()
data = {'a': [int(n) for n in N], 'b': [int(n)**2 for n in N], 'c': [int(n)**3 for n in N]}
print("DataFrame: \n{}".format(pd.DataFrame(data)))
