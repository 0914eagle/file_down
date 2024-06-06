
import heapq
n,s,m,k = map(int, input().split())
a = list(map(int, input().split()))
b = []
for _ in range(s):
  l, r = map(int, input().split())
  b.append([l, r])
h = []
for x in b:
  heapq.heappush(h, x)
temp = []
while len(h) > m:
  x = heapq.heappop(h)
  temp.append([x[0], x[1]])
heapq.heapify(temp)
# print(h)
# print(temp)
vis = [0 for i in range(n + 1)]
while len(h) != 0:
  x = heapq.heappop(h)
  l, r = x[0], x[1]
  # print(x)
  for i in range(l, r + 1):
    vis[i] = 1
# print(vis)
final = []
for i in range(len(vis)):
  if vis[i] == 1:
    final.append(a[i - 1])
# print(final)
for i in range(len(final)):
  final.append(final[i])
  heapq.heapify(final)
  # print(final)
  while len(final) > k:
    heapq.heappop(final)
print(final[0])
