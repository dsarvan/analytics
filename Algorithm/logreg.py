#!/usr/bin/env python3
# File: logreg.py
# Name: D.Saravanan
# Date: 19/11/2020
# Script to implement logistic regression in Python from scratch

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-ticks')

x1 = [2.781086, 1.465489372, 3.396561688, 1.38807018, 3.06407232, 7.627531214, 5.332441248, 6.922596716, 8.675418651, 7.673756466]
x2 = [2.550537003, 2.362125076, 4.400293529, 1.850220317, 3.005305973, 2.759262235, 2.088626775, 1.77106367, -0.242068655, 3.508563011]
y0 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

predicted_y = []
c, m1, m2 = 0.0, 0.0, 0.0
for (x1, x2) in zip(x1, x2):
    y = 1/(1 + np.exp(-(c + m1*x1 + m2*x2)))
    c = c + 0.3 * (y0 - y) * y * (1 - y) * 1.0
    m1 = m1 + 0.3 * (y0 - y) * y * (1 - y) * x1
    m2 = m2 + 0.3 * (y0 - y) * y * (1 - y) * x2

predicted_y.append(y)

#fig, ax = plt.subplots()
#ax.scatter(x1, predicted_y)
#ax.scatter(x2, predicted_y)
#plt.show()
