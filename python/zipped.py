#https://www.hackerrank.com/challenges/zipped/problem
stds, rows = map(int,input().split())

values = []
for _ in range(rows):
    values.append(list(map(float,input().split())))
    
def avg(lst): 
    return sum(lst)/rows 

for val in list(map(avg,list(zip(*values)))):
    print(val)
