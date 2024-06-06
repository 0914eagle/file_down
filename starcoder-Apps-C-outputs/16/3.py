
# first, I solved it by using DFS
# there are four cases.
# 1. a - b, b - c, c - d, d - a
# 2. a - b, b - c, c - a
# 3. a - b, b - a
# 4. a - b, b - c, c - b

n, m = map(int, input().split())
ious = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    ious[a].append((b, c))

visited = [False for _ in range(n)]

def dfs(i, c, visited, ans, ious, ious_cnt, min_v, min_c):
    ans.append((c, i))
    ious_cnt += 1
    visited[i] = True
    for j, d in ious[i]:
        if j != c:
            if not visited[j]:
                min_v = min(min_v, d)
                min_c = min(min_c, d)
                ious_cnt, min_v, min_c = dfs(j, i, visited, ans, ious, ious_cnt, min_v, min_c)
    return ious_cnt, min_v, min_c

ans = []
ious_cnt = 0
for i in range(n):
    if not visited[i]:
        ious_cnt, min_v, min_c = dfs(i, i, visited, ans, ious, ious_cnt, 1000, 1000)
        ans[-1] = (min_v, i)

print(ious_cnt)
for i in range(ious_cnt):
    if ans[i][0] > 0:
        print(ans[i][1], end=' ')
        print(ans[i][0])
