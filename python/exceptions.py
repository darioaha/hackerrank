import sys

n = int(input())

for _ in range(n):
    a,b = input().split()
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code:", "integer division or modulo by zero")
    except:
        print("Error Code:", sys.exc_info()[1])
