
def solve(N, K, plants):
  return 0

N, K = map(int, input().split())
plants = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, K, plants))

