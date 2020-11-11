#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    arr = s.split()
    arr = re.split("( )",s)
    result =[]
    for val in arr:
        elem = val
        elem = elem[0:1].upper()+elem[1:]
        result.append(elem)
    return "".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
