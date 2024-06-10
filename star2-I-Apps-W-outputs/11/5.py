
from collections import defaultdict
from sys import stdin
from sys import stdout
from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(node, parent):
    global cost
    global ways
    global n
    global adj
    if parent != -1:
        cost += costs[node-1]
        ways = (ways * n) % 1000000007
    for child in adj[node]:
        if child != parent:
            dfs(child, node)

def solve(n, costs, m, roads):
    global cost
    global ways
    global adj
    global visited
    global n
    n = n
    adj = defaultdict(list)
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, n+1):
        if not visited[i]:
            cost = 0
            ways = 1
            dfs(i, -1)
            if cost < min_cost:
                min_cost = cost
                min_ways = ways
            elif cost == min_cost:
                min_ways = (min_ways + ways) % 1000000007
    return min_cost, min_ways

def main():
    n = int(stdin.readline())
    costs = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    roads = []
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        roads.append((u, v))
    min_cost, min_ways = solve(n, costs, m, roads)
    stdout.write(str(min_cost) + " " + str(min_ways) + "\n")

if __name__ == "__main__":
    main()

