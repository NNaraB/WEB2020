import math

a = int(input())

isPowerOfTwo = False

for i in range(a):
	if math.pow(2,i) == a:
		isPowerOfTwo = True


if isPowerOfTwo:
	print("YES")
else:
	print("NO")