#!/bin/python3

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        arr = input().split()
        if "insert" in arr:
            idx = int(arr[1])
            val = int(arr[2])
            l.insert(idx,val)
        elif "print" in arr:
            print(l)
        elif "remove" in arr:
            val = int(arr[1])
            l.remove(val)    
        elif "append" in arr:
            val = int(arr[1])
            l.append(val)            
        elif "sort" in arr:
            l.sort()
        elif "pop" in arr:
            l.pop() 
        elif "reverse" in arr:
            l.reverse()