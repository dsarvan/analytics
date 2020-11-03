#!/usr/bin/env Rscript

# binomial distribution
binomial <- function(k, n, p) {
	return(factorial(n)/(factorial(k) * factorial(n - k)) * p**(k) * (1 - p)**(n - k))
}

sum(binomial(28:32, 75, 0.5))
1 - (sum(binomial(0:27, 75, 0.5)) + sum(binomial(33:75, 75, 0.5)))

# compute cumulative distribution function (CDF)
# P(28 <= X <= 32)
sum(dbinom(x = 28:32, size = 75, prob = 0.5))
1 - (sum(dbinom(0:27, 75, 0.5)) + sum(dbinom(33:75, 75, 0.5)))
pbinom(32, size = 75, prob = 0.5) - pbinom(27, size = 75, prob = 0.5)
