#https://www.hackerrank.com/challenges/np-arrays/problem?h_r=next-challenge&h_v=zen
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arrnp = numpy.array(arr,float)
    return arrnp[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)