
import numpy as np
import random
n, m = map(int, input().split())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(m):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print(x,y)
for i in range(n+m-1):
    for j in range(i+1,n+m):
        if np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)<=np.sqrt(2):
            print("YES")
            break
    else:
        continue
    break
else:
    print("NO")
