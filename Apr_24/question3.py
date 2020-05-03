print("Enter 9 elements (1-9) \nFor missing value Enter 0 \n")
count = 0; values = []; mValue = []

while (count < 9):
	data = input("Element {}/9 -> Enter numbers: ".format(count))
	for n in data.split(): 
		if int(n) not in values and int(n) <= 9 or int(n) == 0: values.append(int(n)); count += 1
	print("Current Data: {}".format(values))

print("\nGiven Data: {}".format(values))

for i in range(1,10):
	if i not in values: mValue.append(i)
print("Missing Value: {}".format(mValue))

for m in mValue: nval = [m if n == 0 else n for n in values]
print("After filling the Missing value: {}".format(nval))
