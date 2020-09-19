#!/usr/bin/env python3
# File: visualization.py
# Name: D.Saravanan
# Date: 19/09/2020
# Script to visualize using python matplotlib

import numpy as np
import matplotlib.pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title('Visualization')
plt.show()
