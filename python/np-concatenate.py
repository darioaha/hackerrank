import numpy as np

n,m,p = list(map(int,input().split()))
nparr = np.empty((0, p),int)

for _ in  range(n+m):
    row = list(map(int,input().split()))
    nprow = np.array([row])
    if (nparr.size == 0):
        nparr = np.append(nparr,nprow, axis=0)    
    else:
        nparr = np.concatenate((nparr,nprow), axis=0)    

print(nparr)