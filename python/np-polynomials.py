#https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy as np

arr = np.array(list(map(float,input().split())))
x = float(input())

print(np.polyval(arr, x))


