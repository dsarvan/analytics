import numpy as np
import pandas as pd

N = int(input("Enter the number of terms: "))
alist = []; blist = []; clist = []; dlist = []

for n in range(N):
	alist.append(np.random.randint(0,25))
	blist.append(np.random.randint(25,50))
	clist.append(np.random.randint(50,75))
	dlist.append(np.random.randint(75,100))

data = {'a':[n for n in alist], 'b':[n for n in blist], 'c':[n for n in clist], 'd':[n for n in dlist]}
df = pd.DataFrame(data); df['mean'] = df.mean(axis=1); df['stdev'] = df.std(axis=1)
print(df)
