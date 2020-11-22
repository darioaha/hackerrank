#!/bin/python3
#https://www.hackerrank.com/challenges/2d-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ncol = len(arr[0])
    nrows = len(arr)
    j = 0
    k = 0
    cont = True
    result = []    
    for k in range(0,nrows - 2):
        for j in range(0,ncol-2):
            value = sum(arr[k][j:j+3]) + sum(arr[k+1][j+1:j+2]) + sum(arr[k+2][j:j+3])
            result.append(value)
    return max(result)            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
