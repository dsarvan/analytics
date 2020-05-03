import numpy as np
import pandas as pd
from gapminder import gapminder

df = gapminder.copy()
india = df.loc[df['country'] == 'India']
print(india)
