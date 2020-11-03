#!/usr/bin/env Rscript

# binomial distribution
binomial <- function(k, n, p) {
	return(factorial(n)/(factorial(k) * factorial(n - k)) * p**(k) * (1 - p)**(n - k))
}

binomial(15, 121, 0.1)

# compute probability mass function (PMF)
# P(X = 15)
dbinom(x = 15, size = 121, prob = 0.1)
