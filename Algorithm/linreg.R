#!/usr/bin/env Rscript
# File: linreg.R
# Name: D.Saravanan
# Date: 16/11/2020
# Script to implement linear regression in R from scratch

slope <- function(x, y) {
    sum1 = 0; sum2 = 0
    for(i in 1:length(x)) {
        sum1 = sum1 + (x[i] - mean(x)) * (y[i] - mean(y))
        sum2 = sum2 + (x[i] - mean(x))**2
    }
    return(sum1/sum2)
}

intercept <- function(x, y, m) {
    return(mean(y) - m * mean(x))
}

height <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
weight <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

m <- slope(height, weight)
c <- intercept(height, weight, m)

# predicted weight with values m and c
predicted_y <- c()
for(x in height) {
    y <- m*x + c
    predicted_y <- c(predicted_y, y)
}

residuals <- (weight - predicted_y)
print(sum(residuals))


pdf('/home/saran/Analytics/Notebook/plotlm.pdf')
plot(height, weight, col='blue', xlab='height', ylab='weight', main='linear regression in R')
par(new = TRUE)
plot(height, predicted_y, type='l', col='red', xaxt='n', yaxt='n', xlab=' ', ylab=' ')
dev.off()
#system('open /home/saran/Analytics/Notebook/plotlm.pdf')
