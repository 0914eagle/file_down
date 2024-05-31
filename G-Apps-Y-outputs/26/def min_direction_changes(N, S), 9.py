
def min_direction_changes(N, S):
    prefix_east = [0] * (N + 1)
    prefix_west = [0] * (N + 1)
    
    for i in range(N):
        prefix_east[i + 1] = prefix_east[i] + (S[i] == 'E')
        prefix_west[i + 1] = prefix_west[i] + (S[i] == 'W')
    
    min_changes = float('inf')
    
    for i in range(N):
        changes = prefix_west[i] + (prefix_east[N] - prefix_east[i + 1])
        min_changes = min(min_changes, changes)
    
    return min_changes

# Input
N = int(input())
S = input().strip()

# Output
print(min_direction_changes(N, S))
