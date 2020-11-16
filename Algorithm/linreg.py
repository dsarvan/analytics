#!/usr/bin/env python3
# File: linreg.py
# Name: D.Saravanan
# Date: 16/11/2020
# Script ot implement linear regression in Python from scratch

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

def slope(x, y):
    sum1 = 0; sum2 = 0
    for i in range(len(x)):
        sum1 = sum1 + (x[i] - np.mean(x)) * (y[i] - np.mean(y))
        sum2 = sum2 + (x[i] - np.mean(x))**2
    return sum1/sum2

def intercept(x, y, m):
    return np.mean(y) - m * np.mean(x)

height = [151, 174, 138, 186, 128, 136, 179, 163, 152, 131]
weight = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

m = slope(height, weight)
c = intercept(height, weight, m)

predicted_y = [m*x + c for x in height]
residuals = [x1 - x2 for (x1, x2) in zip(predicted_y, weight)]

plt.plot(height, weight, 'bo')
plt.plot(height, predicted_y, color='red')
plt.grid(True)
plt.show()
