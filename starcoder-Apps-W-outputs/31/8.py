
n=int(input())
s=list(map(int,input().split()))
i=1
t=0
while i<n:
    t+=abs(s[i]-s[i-1])
    i+=1
print(t)
