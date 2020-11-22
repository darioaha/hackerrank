#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
import numpy as np
np.set_printoptions(legacy='1.13')
nparr = np.array(list(map(float,input().split())))
#floor
#ceil
#rint
print(np.floor(nparr))
print(np.ceil(nparr))
print(np.rint(nparr))

