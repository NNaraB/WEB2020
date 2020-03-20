a = int(input())

result = 0

for i in range(2,a):
	if a%i==0:
		result = i
		break


if result == 0:
	result = a
	
print(result)

