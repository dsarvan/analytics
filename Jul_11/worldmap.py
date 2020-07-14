#!/usr/bin/env python3
"""File: worldmap.py
   Name: D.Saravanan
   Date: 14/07/2020
   Cmnt: World Map plot using pygal
"""
import pygal
from pygal.style import LightStyle

worldmap_chart = pygal.maps.world.SupranationalWorld(style=LightStyle)
worldmap_chart.add('Africa', [('africa', 1)])
worldmap_chart.add('Asia', [('asia', 1)])
worldmap_chart.add('Europe', [('europe', 1)])
worldmap_chart.add('North America', [('north_america', 1)])
worldmap_chart.add('South America', [('south_america', 1)])
worldmap_chart.add('Oceania', [('oceania', 1)])
worldmap_chart.add('Antartica', [('antartica', 1)])
worldmap_chart.title = "World Map"

# Render file
worldmap_chart.render_to_file('worldmap.svg')
