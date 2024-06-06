
#1228.py
#https://codeforces.com/problemset/problem/1228/A

import string

a,b,l,r=map(int,input().split())

def nexts(s):
    if s=='z':
        return s
    else:
        return chr(ord(s)+1)

s=''
for i in range(a):
    s+=string.ascii_lowercase[i]

while (l<=r):
    tmp=s[:a]
    if (len(set(tmp))==a):
        print(a)
        exit()
    else:
        s=s[1:]+nexts(s[-1])
        l+=1
        r+=1

print(0)
