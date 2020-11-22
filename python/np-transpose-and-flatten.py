#https://www.hackerrank.com/challenges/np-transpose-and-flatten
import numpy as np

n,m = list(map(int,input().split()))
nparr = np.empty((0, m),int)

for _ in range(n):
    row = list(map(int,input().split()))
    nprow = np.array([row])
    nparr = np.append(nparr, nprow, axis=0)
    
print(nparr.transpose())
print(nparr.flatten())
