import sys
a = int(input())

arr = [int(i) for i in input().split()]

max = -sys.maxsize-1
max2 = -sys.maxsize-1

for i in arr:
	if i >max:
		max = i

for i in arr:
	if i >max2 and i!=max:
		max2 = i


print(max2)