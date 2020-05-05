#!/usr/bin/env python3
# File: prime.py
# Name: D.Saravanan    Date: 13/03/2020
# Python script to indicate whether the numbers from 1 to n is prime or not

n = int(input('Enter n: '))

for i in range(1,n+1):
	if(i/2 == 1 or i%2 != 0):
		if(i/3 == 1 or i%3 != 0):
			if(i/5 == 1 or i%5 != 0):
				if(i/7 == 1 or i%7 != 0):
					print(i, 'is a prime number')

	else:
		print(i, 'is not a prime number')
