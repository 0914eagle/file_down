
import math
l,r = map(int,input().split())
l = int(math.log10(l)) + 1
r = int(math.log10(r)) + 1
l=10**(l-1)
r=10**(r)
s = "123456789"
for i in s:
    a=0
    for j in range(l,r):
        if str(i) in str(j):
            a+=1
    print(a,end=" ")
