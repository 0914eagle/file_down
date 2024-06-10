
def solve(n, b):
  return ' '.join(str(x) for x in range(n))

if __name__ == '__main__':
  n = int(input())
  b = list(map(int, input().split()))
  print(solve(n, b))

