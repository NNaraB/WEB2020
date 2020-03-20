import math
import sys
a = int(input())

arr = [int(i) for i in input().split()]

i = 0
max = -sys.maxsize-1
while i <len(arr):
	if arr[i] > max:
			max = arr[i]
	i = i+1

print(max)