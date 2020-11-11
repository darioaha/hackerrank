# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k= input().split()

result = sorted(list(permutations(s,int(k))))
for val in result:
    print(''.join(val))
