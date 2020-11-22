# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy as np

arr = list(map(int,input().split()))

print(np.zeros(([i for i in arr]),dtype=np.int))
print(np.ones(([i for i in arr]),dtype=np.int))