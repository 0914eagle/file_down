
from collections import defaultdict
def solve(n, a):
    graph = defaultdict(list)
    for i in range(n):
        graph[a[i]].append(i)
    
    for gang, districts in graph.items():
        if len(districts) > 1:
            for i in range(1, len(districts)):
                print(districts[i-1]+1, districts[i]+1)
            return
    print('NO')
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)

