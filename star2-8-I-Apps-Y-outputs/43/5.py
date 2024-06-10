
def get_min_pushes(f, s, g, u, d):
  min_pushes = 0

  while s != g:
    if s + u > g:
      min_pushes += (s - g)
      s = g
    elif s + u < g:
      min_pushes += u
      s += u
    elif s + u == g:
      min_pushes += u
      s += u

  return min_pushes

if __name__ == "__main__":
  f, s, g, u, d = map(int, input().split())
  print(get_min_pushes(f, s, g, u, d))

