
def solve(N, K, M, graph):
  return 0

if __name__ == "__main__":
  N, K, M = map(int, input().split())
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
  print(solve(N, K, M, graph))

