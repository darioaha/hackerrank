vv = input()
arr = list(map(int,input().split()))
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

s=0
f = lambda x: 1 if x in a else(-1 if x in b else 0)

print(sum(map(f,arr)))



