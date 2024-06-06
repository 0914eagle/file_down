
#!/usr/bin/env python
# coding=utf-8
a,b,l,r=map(int,input().split())
ans=l-1
if ans==0:
    ans+=a+b

if ans%(a+b)<=a:
    ans+=a
ans+=r-l+1
print(ans%(a+b))
