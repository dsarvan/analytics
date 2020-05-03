import numpy as np
import pandas as pd

rlist = []; [rlist.append(np.random.randint(0,9)) for n in range(9)] 
print("9 random elemets: \n{}".format(rlist))

nlist = np.array([rlist[i:i+3] for i in range(0, len(rlist), 3)])
print("\n3x3 matrix format: \n{}".format(nlist))

df = pd.DataFrame(nlist, index = ['x', 'y', 'z'], columns = ['a', 'b', 'c'])
print("\nPandas DataFrame format: \n{}".format(df))
