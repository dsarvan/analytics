#!/usr/bin/env python3
# File: multiple1.py
# Name: D.Saravanan    Date: 13/03/2020
# Python script to find multiplicative presistance

num = input('Enter n: ')
count=0

for m in range(1,int(num)):
	while len(str(num)) > 1:
		val=1
		for i in num:
			val=val*int(i)

		count+=1
		num=str(val)
		print(val,'step no.', count)
