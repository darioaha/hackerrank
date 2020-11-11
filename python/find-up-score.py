#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    first = max(arr)
    arr = list(filter(lambda x: x != first, arr))
    print(max(arr))
