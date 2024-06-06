
'''
@author: 
@email: 
'''

from functools import reduce
n,l,r = input().split()
l = int(l)
r = int(r)
n = int(n)

a = n
b = n
c = []

while a>0:
    if a%2:
        c.append(1)
        b = b//2
    else:
        c.append(0)
        b = b//2
    a = b

ans = []
ans.append(c)

while reduce(lambda x,y: x*y, c)!=0:
    b = c.copy()
    c = []
    for i in b:
        c.append(i//2)
        c.append(i%2)
        c.append(i//2)
    ans.append(c)

out = []
for i in ans:
    out.extend(i)

print(out[l-1:r])

