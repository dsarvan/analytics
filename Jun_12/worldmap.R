#!/usr/bin/env R
# File: rworldmap.R
# Name: D.Saravanan
# Date: 12/06/2020
# Comd: World Map in R

require(rworldmap)
data("countryExData", envir = environment())
mapCountryData(joinCountryData2Map(countryExData),
			   nameColumnToPlot = "EPI_regions",
			   catMethod        = "categorical",
			   mapTitle         = "World Map",
			   colourPalette    = "rainbow",
			   missingCountryCol= "lightgrey",
			   addLegend        = FALSE)
