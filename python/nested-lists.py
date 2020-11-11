if __name__ == '__main__':
    lowest = 100
    second = 100
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
    arr2 = set(list(val[1] for val in arr))
    second = sorted(arr2)[1]

    result = []
    for val in arr:
        name = val[0]
        score = val[1]
        if (score == second):
            result.append(name)
    print(*sorted(result),sep="\n")