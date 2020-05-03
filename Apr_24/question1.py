def pascal(m,n): return 1 if (n == 0) or (n == m) else pascal(m-1,n-1) + pascal(m-1, n)
N = int(input("Enter the number of lines: "))
for m in range(N): 
	triangle = []
	for n in range(m+1): triangle.append(pascal(m,n))
	print(triangle)
