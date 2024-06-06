
n=int(input())
a=[int(x) for x in input().split()]
d={}
for i in range(n):
    d[a[i]]=d.get(a[i],0)+1
l=sorted(d.keys())
m=0
for i in range(len(l)):
    if l[i]>=0:break
    if d[l[i]]>1:
        m+=1
        print(l[i],l[i])
        d[l[i]]-=1
    if d[l[i]]>0 and l[i+1]!=l[i]+1:
        m+=1
        print(l[i],l[i]+1)
        d[l[i]]-=1
    if d[l[i]]>0:
        m+=1
        print(l[i],l[i+1])
        d[l[i]]-=1
for i in range(len(l)):
    if l[i]>=0:
        if d[l[i]]>1:
            m+=1
            print(l[i],l[i])
            d[l[i]]-=1
        if d[l[i]]>0:
            m+=1
            print(l[i],l[i]+1)
            d[l[i]]-=1
print(m)
