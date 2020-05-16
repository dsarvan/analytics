#!/usr/bin/env python3

def fact(n):
    fact = 1
    for value in range(1, n+1):
        fact *= value
    return(fact)

print("\n__________Binomial Distribution__________\n")

n = int(input("Number of trials: "))
p = float(input("Probability of getting a success in one trial: "))
option1 = input("Type L for at least, M for at most, E for exact: ")
option2 = input("Type S for success, F for failure: ")

if option2 == 'S':
    x = int(input("Number of success desired: "))
    chosen = 'success'
    k = x

else: 
    x = int(input("Number of failure desired: "))
    chosen = 'failure' 
    k = n-x

if option1 == 'L':
    sum = 0
    while(n >= k):
        sum += fact(n)/(fact(n-k)*fact(k)) * (p)**(k) * (1-p)**(n-k)
        k += 1
    
    print("\nThe probability of getting at least {} {}: {:.4f}\n".format(x, chosen, sum))
    
if option1 == 'M':
    sum = 0
    while(k >= 0):
        sum += fact(n)/(fact(n-k)*fact(k)) * (p)**(k) * (1-p)**(n-k)
        k -= 1

    print("\nThe probability of getting at most {} {}: {:.4f}\n".format(x, chosen, sum))

if option1 == 'E':
    sum = fact(n)/(fact(n-k)*fact(k)) * (p)**(k) * (1-p)**(n-k)
    print("\nThe probability of getting exactly {} {}: {:.4f}\n".format(x, chosen, sum))
