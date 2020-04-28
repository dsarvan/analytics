strn = input("Enter a string: ")
vlst = ['a', 'e', 'i', 'o', 'u']; count = 0
for n in strn.lower(): 
	if(n in vlst): count += 1
print('Number of vowels in "{}" are {}.'.format(strn, count))
