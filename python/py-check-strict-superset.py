#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
arrA = input().split()

n = int(input())

ret = True
for i in range(n):
    subarr = input().split()
    if all(elem in arrA for elem in subarr):
        ret = ret and True
    else:
        ret = ret and False
        break
print(ret)
        