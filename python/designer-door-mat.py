# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = input().split()
N,M = int(N),int(M)
welc = "WELCOME"
pattern = ".|."
dash = "-"

M2 = M//2
N2 = N//2

inc = 1
for i in range(N2):
    ndash = int((M-(3*inc))/2)
    print((ndash*dash)+(inc*pattern)+(ndash*dash))
    inc = inc + 2

ndash = int((M-7)/2)
print((ndash*dash)+(welc)+(ndash*dash))

for i in range(N2):
    inc = inc - 2
    ndash = int((M-(3*inc))/2)
    print((ndash*dash)+(inc*pattern)+(ndash*dash))
