
t=int(input())
l=list(map(int,input().split()))
s=0
for i in range(1,len(l)-1):
    s=s+min(l[i-1],l[i+1])
print(s)
