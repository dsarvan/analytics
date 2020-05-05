#!/usr/bin/env python3
# File: gratio.py
# Name: D.Saravanan    Date: 13/03/2020
# Python script to list 'n' fibonnaci terms and find the Golden Ratio from it

n = int(input('Enter n: '))
x=1;y=1

for i in range(0,n):
	sum = x+y
	gratio=y/x
	print(gratio)
	x,y=y,sum
