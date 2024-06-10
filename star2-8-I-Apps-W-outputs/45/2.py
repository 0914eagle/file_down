
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
    indegree = [0 for i in range(n)]
    outdegree = [0 for i in range(n)]
    for i in range(n):
        for j in adj[i]:
            indegree[j] += 1
            outdegree[i] += 1
    cities = []
    for i in range(n):
        if indegree[i] == outdegree[i]:
            cities.append(i+1)
    print(len(cities))
    for i in range(n):
        for j in adj[i]:
            print(i+1, j+1)

