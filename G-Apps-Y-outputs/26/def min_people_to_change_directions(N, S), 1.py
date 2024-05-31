
def min_people_to_change_directions(N, S):
    min_changes = float('inf')
    total_west = S.count('W')
    
    changes_from_west = 0
    for i in range(N):
        if S[i] == 'W':
            changes_from_west += 1
        if S[i] == 'E':
            min_changes = min(min_changes, changes_from_west)
    
    changes_from_east = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'E':
            changes_from_east += 1
        if S[i] == 'W':
            min_changes = min(min_changes, changes_from_east)
    
    return min_changes

# Input
N = int(input())
S = input().strip()

# Output
print(min_people_to_change_directions(N, S))
