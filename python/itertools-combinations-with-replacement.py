from itertools import combinations_with_replacement
s,k = input().split()

s=sorted(s)
r = sorted(list(combinations_with_replacement(s,int(k))))
for val in r:
    print(''.join(val))
    