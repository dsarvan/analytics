#!/usr/bin/env python3
"""File: bimstec.py
   Name: D.Saravanan
   Date: 19/07/2020
   Cmnt: BIMSTEC countries plot using pygal
"""
import pygal
from pygal.style import LightStyle

bimstec_chart = pygal.maps.world.World(style=LightStyle)
bimstec_chart.add('Bangladesh', [('bd', 1)])
bimstec_chart.add('Bhutan', [('bt', 1)])
bimstec_chart.add('India', [('in', 1)])
bimstec_chart.add('Myanmar', [('mm', 1)])
bimstec_chart.add('Nepal', [('np', 1)])
bimstec_chart.add('Sri Lanka', [('lk', 1)])
bimstec_chart.add('Thailand', [('th', 1)])
bimstec_chart.title = "BIMSTEC"

# Render file
bimstec_chart.render_to_file('bimstec.svg')
