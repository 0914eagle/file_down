
n,m=map(int,input().split())
l=list(map(str,input().split()))
s=0
a=[]
for i in range(0,m):
  a.append(l[i].count(chr(i+65)))
s=0
for i in range(0,m):
  s+=max(a[i])*chr(i+65)
print(s)
