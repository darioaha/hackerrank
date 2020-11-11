#!/bin/python3

from collections import deque


d = deque()
if __name__ == '__main__':
    n = int(input())
    d = deque()
    for _ in range(n):
        arr = input().split()
        meth = arr[0]
        if meth == "append":
            val = int(arr[1])
            d.append(val)            
        elif meth == "appendleft":
            val = int(arr[1])
            d.appendleft(val)
        elif meth == "pop":
            d.pop() 
        elif meth == "popleft":
            d.popleft()
    print(*d,sep=" ")