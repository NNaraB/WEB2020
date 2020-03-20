import math

a = int(input())

i = 1

while i<=a:
	temp = i
	while temp >1:
		if temp%2:
			break
		temp = temp /2
	if temp == 1:
		print(i, end = ' ')
	i = i +1



