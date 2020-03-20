a = int(input())


i= 2

result = 0
while i <=a:
	if a % i == 0:
		result = i
		break
	i = i +1


print(result)