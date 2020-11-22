#https://www.hackerrank.com/challenges/np-shape-reshape/problem?h_r=next-challenge&h_v=zen
import numpy

arr = input().split()

nparr = numpy.array(arr,int)

print(nparr.reshape(3,3))