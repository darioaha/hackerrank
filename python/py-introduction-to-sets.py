def average(array):
    arr = list(set(array))
    n = len(arr)
    s = 0
    for val in arr:
        s = s + int(val)
    return s/n

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)