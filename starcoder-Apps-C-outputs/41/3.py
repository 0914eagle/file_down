
N = int(input())
time = [int(x) for x in input().split()]
deps = []
for i in range(N):
  deps.append([int(x) for x in input().split()])

pre = [-1 for _ in range(N)]
post = [N for _ in range(N)]

ans = float('inf')

def dfs_pre(v):
  global pre
  global post
  global ans
  global deps

  pre[v] = max(post[deps[v][1:]])
  post[v] = pre[v] + time[v]

  if pre[v] == N:
    ans = min(ans, time[v])
  for i in deps[v][1:]:
    dfs_pre(i)

dfs_pre(0)
print(ans)
