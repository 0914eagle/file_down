
from collections import defaultdict
n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(m):
    graph[int(input().split()[0])]

for i in range(1, n + 1):
    if arr[i - 1] == 1:
        for x in graph[i]:
            arr[x - 1] = 0
    else:
        for x in graph[i]:
            arr[x - 1] = 1
if 1 not in arr:
    print("YES")
else:
    print("NO")
