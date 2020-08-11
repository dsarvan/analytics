#!/usr/bin/env python3
import matplotlib.pyplot as plt

def f(x):
    return 2*x+1

xval = []
yval = []

x = 0

while x < 20:
    xval.append(x) 
    yval.append(f(x))
    x = f(x)

print(xval)
print(yval)

plt.plot(xval, yval, 'ro')
plt.grid()
plt.show()
