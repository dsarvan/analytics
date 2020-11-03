#!/usr/bin/env Rscript

x <- dbinom(0:25, 121, 0.1)

pdf("plotr.pdf")
barplot(x, names.arg=0:30, panel.first=grid(), xlab="Number of Successes", ylab="Probability", main="Binomial Distribution (n = 121, p = 0.1)")
dev.off()
