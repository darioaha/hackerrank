bla = int(input())
n = set(map(int, input().split()))
bla = int(input())
b = set(map(int, input().split()))

i = n.intersection(b)
u = n.union(b)

print(len(u.difference(i)))