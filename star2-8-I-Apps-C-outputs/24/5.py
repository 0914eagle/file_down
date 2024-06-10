
import sys
import math

def solve():
    
    # Read input
    roost = list(map(float, input().split()))
    N = int(input())
    hiding_spots = [list(map(float, input().split())) for _ in range(N)]
    
    # Compute distances
    dist = []
    for spot in hiding_spots:
        dist.append(math.sqrt((roost[0] - spot[0])**2 + (roost[1] - spot[1])**2))
    
    # Sort distances
    dist.sort()
    
    # Compute minimum distance
    min_dist = 0.0
    for i in range(N):
        min_dist += dist[i]
    
    return min_dist
    
print(solve())

