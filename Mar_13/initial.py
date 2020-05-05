#!/usr/bin/env python3
# File: initial.py
# Name: D.Saravanan    Date: 13/03/2020
# Python script for initial learning

x=5
print('The value of x is', x, 'and the type of x is', type(x))

institute='Nielit'
print(institute, 'is an Institution of Excellence.')

x,y,z='NIELIT','Chennai','India'
print(x,'is an institue in',y,'which is a city in',z)

""" Example of creating list and appending an element in list """
xlist = ['Nielit', 'Chennai', 'Tamil Nadu']
print(xlist)
xlist.append('India')
print(xlist)

""" Getting input from the user """
data=input("Enter the name: ")
print(data,'Welcome Universe')

""" integer input from the user """
data=int(input("Enter an integer: "))
print('Entered value is',data,'and is of type',type(data))

""" Example of swaping two values """
a,b=5,10
print('The value of a is',a,'and the value of b is',b)
a,b=b,a
print('The swaped value of a is',a,'and the swaped value of b is',b)

""" Type casting """
data=float(input('Enter a float: '))
if(type(data)==<class 'int'>):
	print('You entered an integer instead of float.')
	print('Let me correct for you.')
	print(float(data))
