# Enter your code here. Read input from STDIN. Print output to STDOUT
n , k = map(int,input().split())

arr=[]
for val in range(1,k+1):
    po = val - 1
    arr.append(n**po)

if (sum(arr)== k):
    print(True)
else:
    print(False)