

a = int(input())
arr = []



for i in range(a):
	list = input().split()
	command = list[0]
	values = list[1:]



	if command == "insert":
		arr.insert(int(values[0]), int(values[1]))
	elif command == "remove":
		arr.remove(int(values[0]))
	elif command == "append":
		arr.append(int(values[0]))
	elif command == "sort":
		arr.sort()
	elif command == "pop":
		arr.pop()
	elif command == "reverse":
		arr.reverse()
	else:
		print(arr)