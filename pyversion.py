#!/usr/bin/env python3
# File: pyversion.py
# Name: D.Saravanan
# Date: 18/11/2020
# Script to display the version of python and libraries

import sys
print('Python {}'.format(sys.version[0:5]))

import numpy
print('Numpy {}'.format(numpy.__version__))

import scipy
print('Scipy {}'.format(scipy.__version__))

import matplotlib
print('Matplotlib {}'.format(matplotlib.__version__))

import pandas
print('Pandas {}'.format(pandas.__version__))

import sklearn
print('SKLearn {}'.format(sklearn.__version__))
