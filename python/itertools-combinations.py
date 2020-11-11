# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k = input().split()

s=sorted(s)
for i in range(1,int(k)+1):
    r = sorted(list(combinations(s,i)))
    for val in r:
        print(''.join(val))