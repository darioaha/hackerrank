#https://www.hackerrank.com/challenges/np-min-and-max
import numpy as np

n,m = list(map(int,input().split()))

arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

nparr = np.array(arr)
print(np.max(np.min(nparr, axis = 1)))