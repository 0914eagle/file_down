
#coding=utf-8

from math import sqrt

n=input()
x=[]
y=[]
for i in range(n):
    a,b=map(int,raw_input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

A=0
for i in range(n):
    A+=x[i]*y[i+1]-x[i+1]*y[i]
A=abs(A)/2.0

B=0
for i in range(n):
    B+=x[i]*x[i+1]*(y[i]-y[i+1])
    B+=x[i+1]*y[i+1]*(y[i]-y[i+1])
    B+=x[i]*y[i]*(x[i+1]-x[i])
    B+=x[i+1]*y[i]*(x[i+1]-x[i])
B=abs(B)/6.0

print(A/B)
