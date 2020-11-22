#https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy as np

n = int(input())
A = np.array([list(map(float,input().split())) for _ in range(n)])

print(round(np.linalg.det(A),2))

# Test case
# 2
# 1.1 1.1
# 1.1 1.2

# 0.11