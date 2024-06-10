
h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

for i in range(h):
  a[i].insert(0, '#')
  a[i].append('#')
a.insert(0, ['#'] * (w + 2))
a.append(['#'] * (w + 2))

for i in range(h + 2):
  print(''.join(a[i]))

