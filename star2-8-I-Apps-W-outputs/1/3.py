
def ring_size(w, h):
  return 2*(w+h-4)

w, h, k = map(int, input().split())
print(sum(ring_size(w - 4*i, h - 4*i) for i in range(k)))

