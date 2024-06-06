
import math
n=int(input())
x=[]
y=[]
r=[]
for i in range(n):
    a=list(map(int,input().split()))
    x.append(a[0])
    y.append(a[1])
    r.append(a[2])
max1=0
for i in range(n):
    for j in range(i+1,n):
        max1=max(max1,math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)-(r[i]+r[j]))
print(int(max1*10**9))
