import math
a = int(input())


i = 0

while i<=a:
	if math.pow(2,i)>=a:
		print(i)
		break

	i = i + 1

