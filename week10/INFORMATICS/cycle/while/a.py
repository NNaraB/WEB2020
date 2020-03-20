import math


a = int(input())


i = 0
while i <=a:
	if math.ceil(math.sqrt(i))==math.sqrt(i) and i!=0:
		print(i, end = '\n')
	i=i+1

