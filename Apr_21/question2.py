str = input("Enter multiple string with space delimiter: ")
for n in range(len(str.split())): print("Word {} is {}".format(n+1, str.split()[n]))
