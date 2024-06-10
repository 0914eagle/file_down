
w, h, k = [int(x) for x in input().split()]
result = 0
for i in range(k):
  result += (w - 4 * i) * 2 + (h - 4 * i) * 2 - 4
print(result)

