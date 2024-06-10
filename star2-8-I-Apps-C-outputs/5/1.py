
def solve(N, D, edges):
  adj = [[] for _ in range(N)]
  for i, x in enumerate(edges):
    adj[x].append(i)

  def dfs(node, parent):
    subtrees = [dfs(child, node) for child in adj[node]]
    subtrees.sort(reverse=True)

    best = 0
    for subtree in subtrees:
      best = max(best, subtree)
    if parent is not None:
      best = max(best, D + 1)
    for i, subtree in enumerate(subtrees):
      best = max(best, subtree + i + 1)
    return best

  return dfs(0, None)

N, D = map(int, input().split())
edges = [int(input()) for _ in range(N - 1)]
print(solve(N, D, edges))

