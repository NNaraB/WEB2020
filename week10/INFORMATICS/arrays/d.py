cnt = 0

a = int(input())
list = [int(i) for i in input().split()]

for i in range(len(list)):
	if i+1 <len(list):
		if list[i+1]>list[i]:
			cnt = cnt+1

print(cnt)