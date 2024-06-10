
import sys

def solve(n, a):
  last_visited = [-1] * (max(a) + 1)
  for i in range(n - 1, -1, -1):
    cafe_idx = a[i]
    last_visited[cafe_idx] = i

  min_idx = min(range(len(last_visited)), key=lambda i: last_visited[i])
  return min_idx

def main():
  n = int(input())
  a = list(map(int, input().split()))
  print(solve(n, a))

if __name__ == '__main__':
  main()


