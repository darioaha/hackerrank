from collections import Counter
nv = int(input())
arr = map(int,input().split())

arrCount = Counter(arr)

n = int(input())
total = 0
for _ in range(n):
    s,price = map(int,input().split())
    if (arrCount[s] > 0):
        arrCount[s] = arrCount[s] - 1
        total = total + price

print(total)

