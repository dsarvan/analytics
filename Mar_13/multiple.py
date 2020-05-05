#!/usr/bin/env python3
# File: multiple.py
# Name: D.Saravanan    Date: 13/03/2020
# Python script to find multiplicative presistance

n = input('Enter n: ')
count=0

for num in range(11,int(n)+1): 
    while len(str(num)) > 1:
        val=1
        for i in str(num):
            val=val*int(i)
        count+=1
        num=str(val)

    print(num,'step no.', count)
