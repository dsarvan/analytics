#!/usr/bin/env Rscript

x <- dbinom(25:35, 75, 0.5)

pdf("plot3.pdf")
barplot(x, names.arg=25:35, panel.first=grid(), xlab="Number of Successes", ylab="Probability", main="Binomial Distribution (n = 75, p = 0.5)")
dev.off()
