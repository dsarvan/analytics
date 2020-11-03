#!/usr/bin/env Rscript

# binomial distribution
binomial <- function(k, n, p) {
	return(factorial(n)/(factorial(k) * factorial(n - k)) * p**(k) * (1 - p)**(n - k))
}

sum(binomial(0:23, 30, 0.5))
1 - sum(binomial(24:30, 30, 0.5))

# compute cumulative distribution function (CDF)
# P(X <= 23)
sum(dbinom(x = 0:23, size = 30, prob = 0.5))
1 - sum(dbinom(x = 24:30, size = 30, prob = 0.5))
pbinom(23, size = 30, prob = 0.5)
