# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = list(map(int, input().split()))

def isPalindromic(val):
    if (str(val) == str(val)[::-1]):
        return True


def checkFunction(arr):
    if (any( val < 0 for val in arr)):
        return False
    if (any(isPalindromic(val) for val in arr)):
        return True
    return False

print(checkFunction(arr))