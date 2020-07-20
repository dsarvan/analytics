#!/usr/bin/env python3
"""File: bimstec.py
   Name: D.Saravanan
   Date: 20/07/2020
   Cmnt: G20 countries plot using pygal
"""
import pygal
from pygal.style import Style

custom_style = Style(colors=('#adcbe3', '#bfb5b2'))

g20_chart = pygal.maps.world.World(style=custom_style)
g20_chart.add('G20 Advanced Economies', ['au','ca','fr','de','it','jp','kr','gb','us'])
g20_chart.add('G20 Emerging Economies', ['ar','br','cn','in','id','mx','ru','sa','za','tr'])
g20_chart.title = "G20 Nations"

# Render file
g20_chart.render_to_file('g20.svg')
