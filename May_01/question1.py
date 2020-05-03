#!/usr/bin/env python3
import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()

N = int(input("Enter the number of countries to display: "))
w = input("Enter Y to display the top {} countries based on GDP: ".format(N))
