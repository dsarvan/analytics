#!/usr/bin/env python3
# File: lorentz.py
# Name: D.Saravanan    Date: 19/03/2020
# Python script for lorentz system

import numpy as np
import matplotlib.pyplot as plt

x0,y0,z0 = 1,1,1
delt = 0.01
sigma=10;beta=8/3;rho=28 

x=[]; y=[]; z=[]

for n in range(10000):
	x1 = delt*(sigma*(y0-x0))+x0
	y1 = delt*(x0*(rho-z0)-y0)+y0
	z1 = delt*(x0*y0-beta*z0)+z0
	x.append(x1); y.append(y1); z.append(z1)
	x0=x1;y0=y1;z0=z1

plt.subplot(1,3,1)
plt.plot(x,z,color='darkslateblue',label='x-z')
plt.xlabel('x')
plt.ylabel('z')
plt.title('x-z plot')
plt.legend()

plt.subplot(1,3,2)
plt.plot(y,z,color='darkslateblue',label='y-z')
plt.xlabel('y')
plt.ylabel('z')
plt.title('y-z plot')
plt.legend()

plt.subplot(1,3,3)
plt.plot(y,x,color='darkslateblue',label='y-x')
plt.xlabel('y')
plt.ylabel('x')
plt.title('y-x plot')
plt.legend()

plt.show()
