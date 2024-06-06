
n,k=map(int,input().split())
a=list(map(int,input().split()))

count=[0]*k
for i in range(n):
    count[a[i]-1]+=1

if sum(count)!=n:
    print('NO')
    exit()

print('YES')
for i in range(n):
    ans=[]
    for j in range(k):
        for _ in range(count[j]):
            ans.append(j+1)
            count[j]-=1
        if count[j]<0:
            print('NO')
            exit()
    print(*ans)
