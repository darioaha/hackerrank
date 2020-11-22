#https://www.hackerrank.com/challenges/np-mean-var-and-std
import numpy as np

n,m = list(map(int,input().split()))

arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

nparr = np.array(arr)

# The mean along axis 1
# The var along axis 0
# The std along axis None
print(np.mean(nparr, axis = 1))
print(np.var(nparr, axis = 0))
print(np.around(np.std(nparr, axis = None), decimals = 11))

