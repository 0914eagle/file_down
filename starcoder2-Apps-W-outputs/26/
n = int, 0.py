
n = int(input())
p = list(map(int,input().split()))

ans = []
for i in range(n-1):
    for j in range(i,n):
        if p[i] > p[j]:
            p[i],p[j] = p[j],p[i]
            ans.append(j+1)

print(len(ans))
for i in ans:
    print(i)
