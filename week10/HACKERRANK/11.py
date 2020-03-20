import sys
from decimal import Decimal
dictionary = {
	
}

a = int(input())
min = sys.maxsize
min2 = sys.maxsize
listNames = []
for i in range(a):
	name = input()
	score=Decimal(input())
	if score<min:
		min = score
	dictionary[name] = score


for i in dictionary.values():
	if i <min2 and i!=min:
		min2 = i

for name,score in dictionary.items():
	if score == min2:
		listNames.append(name)


listNames.sort()

for name in listNames:
	print(name)





