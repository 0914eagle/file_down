
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n, k1, k2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

h = []
for i in range(n):
    heappush(h, -abs(A[i] - B[i]))

for _ in range(k1 + k2):
    x = heappop(h)
    if x > 0:
        heappush(h, x - 2)
    else:
        heappush(h, x + 2)

print(-sum(h))

