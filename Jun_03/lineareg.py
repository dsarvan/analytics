#!/usr/bin/env python3
""" 
File: lineareg.py
Name: D.Saravanan
Date: 04/06/2020
Comt: Linear Regression in Python
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Salary_Data.csv")

x = df.iloc[:,0]
y = df.iloc[:,1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3)

x_train = np.array(x_train); x_test = np.array(x_test)
y_train = np.array(y_train); y_test = np.array(y_test)

x_train = x_train.reshape(1, -1); x_test = x_test.reshape(1, -1)
y_train = y_train.reshape(1, -1); y_test = y_test.reshape(1, -1)

reg = LinearRegression()
print(reg.fit(x_train, y_train))

#x_pred = reg.predict(y_test)
#y_pred = reg.predict(x_test)

#plt.plot(x, y, 'r--o')
#plt.plot(x, y_pred, 'b--o')
#plt.show()
