list=[]
for n in range(1,4):
	list.append(int(input('Enter the value: ')))
list.sort()
print('The minimum value is ', list[0]) # for minimum value
print('The maximum value is ', list[-1]) # for maximum value
