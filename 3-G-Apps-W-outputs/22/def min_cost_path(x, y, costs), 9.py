
import sys

def min_cost_path(x, y, costs):
    min_cost = float('inf')
    
    # Calculate the minimum cost by considering all possible paths
    for i in range(6):
        dx = [1, 1, 0, -1, -1, 0]
        dy = [0, -1, -1, 0, 1, 1]
        
        nx = 0
        ny = 0
        cost = 0
        
        while nx != x or ny != y:
            nx += dx[i]
            ny += dy[i]
            cost += costs[i]
            min_cost = min(min_cost, cost + abs(nx - x) * costs[2] + abs(ny - y) * costs[5])
    
    return min_cost

# Read input
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    costs = list(map(int, input().split()))
    
    # Calculate and print the minimum cost for each test case
    print(min_cost_path(x, y, costs))
