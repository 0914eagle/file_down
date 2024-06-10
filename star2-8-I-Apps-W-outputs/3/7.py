
def minRemove(table):
  m = len(table[0])
  for i in range(m):
    col = [row[i] for row in table]
    if col != sorted(col):
      return i
  return m
n, m = map(int, input().split())
table = [input() for i in range(n)]
print(minRemove(table))

