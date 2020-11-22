# https://www.hackerrank.com/challenges/py-check-subset/problem
n=int(input())

for _ in range(n):
    n1=input()
    arr1=input().split()
    n2=input()
    arr2=input().split()
    if all(elem in arr2 for elem in arr1):
        print(True)
    else:
        print(False)
    