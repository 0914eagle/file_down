
n,m,h = map(int, input().split())

time = list(map(int, input().split()))

client = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    client[a].append(b)
    client[b].append(a)

ans = []

for i in range(1,n+1):
    flag = True
    for j in client[i]:
        if time[i-1] == time[j-1]:
            flag = False
            break
    if flag:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i, end=' ')
print()
