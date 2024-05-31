
def min_moves_to_equalize_matches(n, matchboxes):
    total_matches = sum(matchboxes)
    target_matches = total_matches // n
    moves = 0
    
    for i in range(n-1):
        diff = matchboxes[i] - target_matches
        matchboxes[i+1] += diff
        moves += abs(diff)
    
    return moves

# Input
n = int(input())
matchboxes = list(map(int, input().split()))

# Output
print(min_moves_to_equalize_matches(n, matchboxes))
