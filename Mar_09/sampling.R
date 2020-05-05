#!/usr/bin/env Rscript
# File: sampling.R
# Name: D.Saravanan    Date: 09/03/2020
# R script for sampling

airq <- airquality

for(m in seq(2,20,1)) {

	dframe <- data.frame(table(cut(airq$Temp,m)))

	for(n in seq(1,m,1)) {

		cnum <- substring(dframe$Var1[n],2,14)
		cnum <- strsplit(cnum,"]")
		cnum <- strsplit(unlist(cnum),",")
		cnum <- strsplit(unlist(cnum)," ")

		num1 <- as.numeric(cnum[1])
		num2 <- as.numeric(cnum[2])
		  
		Mean <- (num1+num2)/2
		dframe$X[n] <- with(dframe, Mean)
		dframe$Freq.X <- with(dframe, dframe$Freq*dframe$X)
		dframe$X2 <- with(dframe, dframe$X**2)
		dframe$Freq.X2 <- with(dframe, dframe$Freq*dframe$X2)

	}

	print(dframe)
	sumFreq.X <- sum(dframe$Freq.X)
	sumFreq.X2 <- sum(dframe$Freq.X2)
	sumFreq <- sum(dframe$Freq)

	mn <- sumFreq.X/sumFreq
	var <- (sumFreq.X2/sumFreq)-(sumFreq.X/sumFreq)**2
	sd <- sqrt(var)

	print(paste("Mean: ", mn))
	print(paste("Variance: ", var))
	print(paste("Standard Deviation: ", sd))
	cat("\n")
}
