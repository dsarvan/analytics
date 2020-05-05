#!/usr/bin/env Rscript

airq <- airquality

dframe <- data.frame(table(cut(airq$Temp,5)))

for(n in seq(1,5,1)) {

	cnum <- substring(dframe$Var1[n],2,14)
	cnum <- strsplit(cnum, "]")
	cnum <- strsplit(unlist(cnum), ",")
	cnum <- strsplit(unlist(cnum), " ")

	num1 <- as.numeric(cnum[1])
	num2 <- as.numeric(cnum[2])

	Mean <- (num1+num2)/2

	dframe$X[n] <- with(dframe, Mean)
}

print(dframe)
