v = int(input())
t = int(input())

if v>0:
	result = v*t-109
else:
	result = 109 + v*t

print(result)