
n=int(input())
a=[input() for i in range(n)]
a.sort()
l=list(a[0])
r=list(a[n-1])
for i in range(n-1):
    l1=list(a[i])
    r1=list(a[i+1])
    for j in range(len(l1)):
        if l1[j]!=r1[j]:
            l.append(l1[j])
            r.append(r1[j])
            break
s=list(set(l+r))
s.sort()
d={}
for i in range(len(s)):
    d[s[i]]=i
z=""
for i in range(len(l)):
    z+=chr(97+d[l[i]])
print(z)
