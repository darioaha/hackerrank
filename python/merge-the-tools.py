def merge_the_tools(string, k):
    # your code goes here
    arr = list(string)
    init = 0
    while init <= len(arr):
        arrPrint = list(dict.fromkeys(arr[init:init+k]))
        if (len(arrPrint)<1):
            break
        print(''.join(arrPrint))
        init = init + k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)