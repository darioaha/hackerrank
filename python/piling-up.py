
from collections import deque

def pilingUp(arr,left,eq):
    last = int()
    if (left and not eq):
        last= arr.popleft()
    elif (not left and not eq):
        last = arr.pop()
    elif (eq):
        if len(pilingUp(arr,True,False)) == 0 or len(pilingUp(arr,False,False)) == 0:
            return []

    if len(arr)==1 and arr[0] <= last:
        return []
    elif len(arr)==1 and arr[0] > last:
        return arr
    elif len(arr)>1:
        if arr[0] > arr[-1] and arr[0] <= last:
            pilingUp(arr,True,False)
        elif arr[0] < arr[-1] and arr[1] <= last:
            pilingUp(arr,False,False)
        elif arr[0] == arr[-1] and arr[0] <= last:
            pilingUp(arr,False,True)
    
    return arr

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        nc = int(input())        
        arrC = deque(map(int, input().split()))
        arr.append(arrC)
    
    result = []
    for d in arr:
        if (len(d)<=2):
            result.append([])
            continue

        if d[0] > d[-1]:
            # print("appendTrue")
            result.append(pilingUp(d,True,False))
        elif d[0] < d[-1]:
            # print("appendFalse")
            result.append(pilingUp(d,False,False))
        elif d[0] == d[-1]:
            result.append(pilingUp(d,False,True))
    
    for val in result:
        if len(val) > 0:
            print("No")
        else:
            print("Yes")
            
