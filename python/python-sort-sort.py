#!/bin/python3

import math
import os
import random
import re
import sys

def keyFunc(item,k):
    return item[k]

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr[::])
    k = int(input())
    # arr.sort(key=keyFunc(k))
    arr.sort(key=lambda x: x[k])
    
    print('\n'.join([' '.join(['{}'.format(item) for item in row]) 
      for row in arr]))

