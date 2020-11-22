# https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby

S = input()
key_func = lambda x: x[0] 

tuples=[]
for k, g in groupby(S, key_func):
    tuples.append((len(list(g)), int(k)))

print(*tuples)