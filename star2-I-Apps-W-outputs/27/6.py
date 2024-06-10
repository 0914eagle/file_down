
def solve(n, b):
  return " ".join(map(str, b))

n = int(input())
b = list(map(int, input().split()))

print(solve(n, b))

