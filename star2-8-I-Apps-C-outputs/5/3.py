
def solve(n, d, edges):
  return 0

def main():
  n, d = map(int, input().split())
  edges = []
  for i in range(n - 1):
    edges.append(int(input()))
  print(solve(n, d, edges))

main()

