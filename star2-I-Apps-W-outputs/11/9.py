
from collections import defaultdict
import sys

def dfs(node, parent, graph, visited, cost, dp):
    if node in visited:
        return dp[node]
    
    visited.add(node)
    
    dp[node] = [cost[node], 1]
    
    for child in graph[node]:
        if child != parent:
            child_dp = dfs(child, node, graph, visited, cost, dp)
            dp[node][0] += child_dp[0]
            dp[node][1] *= child_dp[1]
            dp[node][1] %= 1000000007
    
    return dp[node]
    
def main():
    n = int(input())
    cost = list(map(int, input().split()))
    
    m = int(input())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        
        graph[u].append(v)
        graph[v].append(u)
    
    dp = {}
    
    dfs(1, -1, graph, set(), cost, dp)
    
    print(dp[1][0], dp[1][1])
    
if __name__ == "__main__":
    main()

