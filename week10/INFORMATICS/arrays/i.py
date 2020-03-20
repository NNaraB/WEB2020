a = int(input())

arr = [int(i) for i in input().split()]

i = 0
temp = 0
while i < len(arr):

	if i == 0:
		temp = arr[i]
		arr[i] = arr[i-1] # 1 2 3 4 5 6
	else:
		temp2 = arr[i]
		arr[i] = temp
		temp = temp2




	i = i +1

i = 0
while i <len(arr):
	print(arr[i], end = ' ')

	i = i +1