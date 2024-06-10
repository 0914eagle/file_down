
h = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
h.sort(reverse=True)
b.sort(reverse=True)
n = 0
while h and b:
  if h[0] > b[0]:
    n += h[0] // b[0]
    h[0] %= b[0]
  elif h[0] < b[0]:
    n += b[0] // h[0]
    b[0] %= h[0]
  else:
    n += 1
    h.pop(0)
    b.pop(0)
print(n)

