#https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy as np

n,m = list(map(int,input().split()))

arr1 = np.array([list(map(int,input().split())) for i in range(n)],dtype=np.int)
arr2 = np.array([list(map(int,input().split())) for i in range(n)],dtype=np.int)

print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.floor_divide(arr1, arr2))
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))

# unlock testcase
# 2 4
# 1 2 3 4
# 1 2 3 4
# 5 6 7 7
# 5 6 7 7