
import sys

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

print(a[1]*b[0])
