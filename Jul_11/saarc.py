#!/usr/bin/env python3
"""File: saarc.py
   Name: D.Saravanan
   Date: 14/07/2020
   Cmnt: SAARC countries plot using pygal
"""
import pygal
from pygal.style import LightStyle

saarc_chart = pygal.maps.world.World(style=LightStyle)
saarc_chart.add('Afghanistan', [('af', 1)])
saarc_chart.add('Bangladesh', [('bd', 1)])
saarc_chart.add('Bhutan', [('bt', 1)])
saarc_chart.add('India', [('in', 1)])
saarc_chart.add('Malidves', [('mv', 1)]) 
saarc_chart.add('Nepal', [('np', 1)])
saarc_chart.add('Sri Lanka', [('lk', 1)])
saarc_chart.add('Pakistan', [('pk', 1)])
saarc_chart.title = "SAARC"

# Render file
saarc_chart.render_to_file('saarc.svg')
