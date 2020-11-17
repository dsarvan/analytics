#!/usr/bin/env Rscript
# File: linreg.R
# Name: D.Saravanan
# Date: 16/11/2020
# Script to implement linear regression in R from scratch

# estimating the slope
slope <- function(x, y, n) {
    sum1 = 0; sum2 = 0
    for(i in 1:n) {
        sum1 = sum1 + (x[i] - mean(x)) * (y[i] - mean(y))
        sum2 = sum2 + (x[i] - mean(x))**2
    }
    return(sum1/sum2)
}

# estimating the intercept
intercept <- function(x, y, m) {
    return(mean(y) - m * mean(x))
}

height <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
weight <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

n <- length(height)
m <- slope(height, weight, n)
c <- intercept(height, weight, m)

# predicted weight with values m and c
predicted_y <- c()
for(x in height) {
    y <- m*x + c
    predicted_y <- c(predicted_y, y)
}

# error estimation (Root Mean Squared Error)
rmse <- function(p, y, n) {
    sum = 0
    for(i in 1:n) {
        sum = sum + (p[i] - y[i])**2
    }
    return(sqrt(sum/n))
}

residuals <- (predicted_y - weight)
print(sum(residuals))

err <- rmse(predicted_y, weight, n)
print(err)

pdf('/home/saran/Analytics/Notebook/plotlm.pdf')
plot(height, weight, col='blue', xlab='height', ylab='weight', main='linear regression in R')
par(new = TRUE)
plot(height, predicted_y, type='l', col='red', xaxt='n', yaxt='n', xlab=' ', ylab=' ')
dev.off()
system('zathura /home/saran/Analytics/Notebook/plotlm.pdf')
