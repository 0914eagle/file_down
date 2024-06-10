
n = int(input())
a = list(map(int, input().split()))

def dfs(u, p):
    for v in range(1, n+1):
        if v == u or v == p: continue
        if a[v-1] == u:
            return True
    return False

ans = 1
for i in range(n):
    if dfs(i+1, a[i]-1):
        ans = 0
        break
print(ans)

