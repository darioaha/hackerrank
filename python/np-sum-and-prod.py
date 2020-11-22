#https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy as np

n,m = list(map(int,input().split()))

arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

nparr = np.array(arr)
npsum = np.sum(nparr, axis=0)
print(np.prod(npsum))

