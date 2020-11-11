# Enter your code here. Read input from STDIN. Print output to STDOUT

k, M = map(int,input().split())

Smax = 0
for _ in range(k):
    arr = list(map(int,input().split()))
    s = max(map(lambda x : x%M, arr))
    idx = arr.index(s)
    Smax += arr[idx]**2

print(Smax%M)
