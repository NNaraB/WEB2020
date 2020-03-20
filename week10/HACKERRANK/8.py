import numpy as np



a = np.array([int(i) for i in input().split()])
b= np.array([int(i) for i in input().split()])

print (np.inner(a,b))
print (np.outer(a,b))