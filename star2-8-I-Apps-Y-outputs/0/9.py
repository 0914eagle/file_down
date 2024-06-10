
def solve(s):
  x = 0
  y = 0
  for ch in s:
    if ch == 'L':
      x -= 1
    elif ch == 'R':
      x += 1
    elif ch == 'U':
      y += 1
    else:
      y -= 1
  return x == 0 and y == 0


def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    left = 0
    right = n
    while left < right:
      mid = (left + right) // 2
      if solve(s[:mid + 1]):
        right = mid
      else:
        left = mid + 1
    if left == n:
      print(-1)
    else:
      print(left + 1, right + 1)


if __name__ == '__main__':
  main()


