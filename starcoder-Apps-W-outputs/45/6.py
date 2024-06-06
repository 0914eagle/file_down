
from math import *
def e(a,b):
    return a if a==b else 0.5
def f(l):
    return 1 if l==1 else (1-e(0,l[-1]))*f(l[:-1])+e(0,l[-1])
def g(s1,s2):
    i=0
    j=0
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            i+=1
            j+=1
        elif s2[j]=="?":
            i+=1
            j+=1
    while i<len(s1):
        if s1[i]=="+":
            return 1
        elif s1[i]=="-":
            return -1
        i+=1
    return 0
def solve(s1,s2):
    l=[]
    for i in range(len(s2)):
        if s2[i]=="?":
            l.append(0)
            l.append(1)
        elif s2[i]=="+":
            l.append(1)
        else:
            l.append(-1)
    return f(l)*e(g(s1,s2),0)
s1=list(input())
s2=list(input())
print(solve(s1,s2))
