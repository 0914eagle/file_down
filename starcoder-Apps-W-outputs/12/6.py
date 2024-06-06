
n,t,c = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
s=0
for i in range(len(a)):
    if a[i]<=t:
        s+=1
print(s)
