
n,k=[int(i) for i in input().split()]

c=[int(i) for i in input().split()]
c.sort()

ans=[]
j=0
for i in range(n):
    while j<n and c[j]+c[i]<=k:
        j+=1
    ans.append(k-c[i])

print(len(ans))
print(*ans)
