#https://www.hackerrank.com/challenges/np-dot-and-cross
import numpy as np

n = int(input())
A = np.array([list(map(int,input().split())) for i in range(n)])
B = np.array([list(map(int,input().split())) for i in range(n)])

# print(A)
print(np.dot(A, B))