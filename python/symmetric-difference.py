mc = input()
m = set(list(map(int,input().split())))
nc = input()
n = set(list(map(int,input().split())))

ndiffm = n.difference(m)
mdiffn = m.difference(n)

result = ndiffm.union(mdiffn)
for val in sorted(result):
    print(val)

