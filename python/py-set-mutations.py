bla = input()
s = set(input().split())
n = int(input())

for _ in range(n):
    inp = input().split()
    s2 = set(input().split())
    cmd = inp[0]
    if cmd == "update":
        s.update(s2)
    elif cmd == "intersection_update":
        s.intersection_update(s2)
    elif cmd == "symmetric_difference_update":
        s.symmetric_difference_update(s2)
    elif cmd == "difference_update":
        s.difference_update(s2)

print(sum(map(int,list(s))))