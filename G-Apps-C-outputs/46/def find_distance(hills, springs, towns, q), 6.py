
import math

def find_distance(hills, springs, towns, q):
    def dist(h1, h2):
        x1, y1, h1 = hills[h1]
        x2, y2, h2 = hills[h2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + max(0, h2 - h1) ** 2)
    
    n = len(hills)
    s = len(springs)
    t = len(towns)
    
    distances = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        distances[i][i] = 0
        
    for i in range(n):
        for j in range(i+1, n):
            distances[i][j] = distances[j][i] = dist(i, j)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    min_length = float('inf')
    for perm in itertools.permutations(range(s), t):
        length = 0
        for i in range(t):
            length += distances[springs[perm[i]]][towns[i]]
        
        if length <= q:
            min_length = min(min_length, length)
    
    if min_length == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_length

# Read input
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the result
result = find_distance(hills, springs, towns, q)
print(result)
