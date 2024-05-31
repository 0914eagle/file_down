
def calculate_moves(n, matchboxes):
    total_matches = sum(matchboxes)
    matches_per_box = total_matches // n
    
    moves = 0
    for i in range(n-1):
        diff = matches_per_box - matchboxes[i]
        matchboxes[i] += diff
        matchboxes[i+1] -= diff
        moves += abs(diff)
    
    return moves

# Input
n = int(input())
matchboxes = list(map(int, input().split()))

# Output
print(calculate_moves(n, matchboxes))
