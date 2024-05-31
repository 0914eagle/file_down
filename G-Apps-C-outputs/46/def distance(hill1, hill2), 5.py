
import math
import itertools

def distance(hill1, hill2):
    x1, y1, _ = hill1
    x2, y2, _ = hill2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve_aqueduct(n, s, t, q, hills, springs, towns):
    
    min_total_length = float('inf')
    permutations = list(itertools.permutations(range(s), t))
    
    for perm in permutations:
        total_length = 0
        for i, town in enumerate(towns):
            spring = springs[perm[i]]
            length = distance(hills[town-1], hills[spring-1])
            total_length += length
            if total_length > q:
                break
                
        if total_length <= q:
            min_total_length = min(min_total_length, total_length)

    if min_total_length == float('inf'):
        return "IMPOSSIBLE"
    else:
        return round(min_total_length, 6)

# Reading input
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Calling the function and printing the output
print(solve_aqueduct(n, s, t, q, hills, springs, towns))
