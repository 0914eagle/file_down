
n,p,k=list(map(int,input().split()))
t=list(map(int,input().split()))
times=[0]*(n+1)
for i in range(n):
    times[i+1]=t[i]
for i in range(1,n+1):
    times[i]=times[i]-times[i-1]
total=0
for i in range(n+1):
    if i%2==0:
        total+=times[i]
    else:
        total+=(times[i]*(100+p)/100)
print(total)

