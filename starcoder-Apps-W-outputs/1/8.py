
n,m = map(int, input().split())
graph = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
if n % 2 == 0:
    res = [0] * (n//2)
    for i in range(n//2):
        if len(graph[i]) == 1 or len(graph[n-1-i]) == 1:
            res[i] = False
        else:
            res[i] = True
    if sum(res) == n//2:
        print('Yes')
    else:
        print('No')
else:
    res = [0] * (n//2)
    for i in range(n//2):
        if len(graph[i]) == 1 or len(graph[n-1-i]) == 1:
            res[i] = False
        else:
            res[i] = True
    if sum(res) == n//2:
        print('Yes')
    else:
        print('No')
