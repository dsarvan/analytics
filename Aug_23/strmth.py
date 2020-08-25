#!/usr/bin/env python3
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family']='serif'
plt.style.use('seaborn-dark')

import pdb

file = open('LICENSE.txt', 'r')
pdb.set_trace()
str = file.read()
str = str.lower()
str = str.split()

#list = []
#for word in str:
#    list.append(str.count(word))
#     
#xvalues = []
#for n in range(len(list)):
#    xvalues.append(n+1)

# list comphrension

list = [str.count(word) for word in str]
xvalues = [n+1 for n in range(len(list))]

plt.figure()
plt.plot(xvalues, list, 'bo-')
plt.xlim(0, len(xvalues)+1)
plt.ylim(0, max(list)+1)
plt.title('Frequency of a string based on index position')
plt.xlabel('Index position of a string')
plt.ylabel('Count of the number of occurences of a string')
plt.grid(True); plt.show()
