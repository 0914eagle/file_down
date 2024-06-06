
import math
a=int(input())
l,r=map(int,input().split())

def f(x,a):
    if x>1:
        return f(x//2,a)+f((x+1)//2,a)+f(x%2,a)
    return a

res=[]

for i in range(0,l-1):
    x=math.floor(a/math.pow(2,i))
    res.append(f(x,0))

for i in range(l-1,r):
    x=math.floor(a/math.pow(2,i))
    res.append(f(x,0))

print(res[l-1:r])

print(sum(res[l-1:r]))
