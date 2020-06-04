#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# create a dataframe
df = pd.read_csv("Salary_Data.csv")

# read x and y values
x = df.iloc[:,0]
y = df.iloc[:,1]

# number of rows
n = df.size//2

# summation of x and y 
sum_x = df.iloc[:,0].sum()
sum_y = df.iloc[:,1].sum()

# summation of x.y
sum_xy = (df.iloc[:,0] * df.iloc[:,1]).sum()

# compute theta_1 and theta_2 values
theta2 = (sum_xy - n*np.mean(x)*np.mean(y))/(sum(x**2) - n*np.mean(x)**2)
theta1 = (n*np.mean(x)*np.mean(y) - theta2*n*np.mean(x)**2)/(n*np.mean(x))

epsilon = [(y - theta1 - theta2*x)**2 for x,y in zip(x,y)]

print(epsilon)
print(sum(epsilon))

cal_y = [theta2*x + theta1 for x in x]

plt.plot(x, y, 'r--o', label='Observed Value')
plt.plot(x, cal_y, 'b--o', label='Calculated Value')
plt.legend()
plt.show()
