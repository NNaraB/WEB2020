a = int(input())

arr = [int(i) for i in input().split()]

i = 0
while i <len(arr)-1:
	temp = arr[i+1]
	arr[i+1] = arr[i]
	arr[i] = temp
	i = i+2
i = 0
while i < len(arr):
		print(arr[i], end = ' ')

		i = i +1 