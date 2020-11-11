from collections import defaultdict

n, m = list(map(int, input().split()))
d = defaultdict(list)

for idx in range(n):
    val = str(input())
    d[val].append(idx+1)

for i in range(m):
    group = input()
    if len(d[group])>0:
        print(*d[group])
    else:
        print(-1)
