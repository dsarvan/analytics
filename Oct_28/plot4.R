#!/usr/bin/env Rscript

x <- dbinom(0:20, 25, 0.5)

pdf("plot4.pdf")
barplot(x, names.arg=0:20, panel.first=grid(), xlab="Number of Successes", ylab="Probability", main="Binomial Distribution (n = 25, p = 0.5)")
dev.off()
