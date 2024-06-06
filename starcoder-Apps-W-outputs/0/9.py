
import sys
sys.stdin=open('sample.txt','r')
n,m=[int(x) for x in input().split()]
e=[int(x) for x in input().split()]
d=[[] for x in range(n)]
for i in range(m):
    x,y=[int(x) for x in input().split()]
    d[x].append(y)
l=0
for i in range(n):
    if(e[i]==0):
        l=l+1
a=0
for i in range(n):
    if(e[i]==1):
        for j in range(len(d[i])):
            if(e[d[i][j]]==0):
                a=a+1
print(a+l)
