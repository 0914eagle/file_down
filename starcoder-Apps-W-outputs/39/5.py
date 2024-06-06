
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n, s, m, k = map(int, readline().split())
a = list(map(int, readline().split()))
seg = [[] for _ in range(n+1)]
for _ in range(s):
    l, r = map(int, readline().split())
    seg[l].append(r)

ok, ng = -1, n + 1

while ng - ok > 1:
    mid = (ok + ng) // 2
    b = [i for i in a]
    for i in range(1, n+1):
        for r in seg[i]:
            b[i-1:r] = sorted(b[i-1:r], reverse=True)
    if sum([1 for i in range(n) if b[i] <= b[mid]]) >= k:
        ng = mid
    else:
        ok = mid
print(b[ok] if ng == n+1 else -1)

