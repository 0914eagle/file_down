
# 100%
n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        a[j][i] = a[i][j]

def disparity(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    max_a = max(a)
    max_b = max(b)
    max_ab = max(max_a, max_b)
    for i in range(len(a)):
        a[i] = max_ab - a[i]
    for i in range(len(b)):
        b[i] = max_ab - b[i]
    return max_ab

def solve(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    max_a = max(a)
    max_b = max(b)
    max_ab = max(max_a, max_b)
    for i in range(len(a)):
        a[i] = max_ab - a[i]
    for i in range(len(b)):
        b[i] = max_ab - b[i]
    return max_ab

def dfs(a, b, i):
    if i == n:
        return solve(a, b)
    return min(dfs(a + [a[i]], b, i+1), dfs(a, b + [b[i]], i+1))

print(dfs([], [], 0))
