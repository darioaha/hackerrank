n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    inp = input().split()
    cmd = str(inp[0])
    if cmd == "remove":
        val = int(inp[1])
        s.remove(val) # try catch (?)
    elif cmd == "discard":
        val = int(inp[1])
        s.discard(val)
    elif cmd == "pop":
        s.pop()

print(sum(s))
