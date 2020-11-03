#!/usr/bin/env Rscript

x <- dbinom(0:25, 30, 0.5)

pdf("plot2.pdf")
barplot(x, names.arg=0:25, panel.first=grid(), xlab="Number of Successes", ylab="Probability", main="Binomial Distribution (n = 30, p = 0.5)")
dev.off()
