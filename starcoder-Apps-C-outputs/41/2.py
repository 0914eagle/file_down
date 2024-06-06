
n = int(input())
t = list(map(int,input().split()))
ans = []

for i in range(n):
    j = 0
    j = max(t[i],t[0])
    for k in range(len(ans)):
        j = max(j,ans[k]+t[i])
    ans.append(j)
print(max(ans))
