
def calculate_moves(n, matchboxes):
    total_matches = sum(matchboxes)
    matches_per_box = total_matches // n
    moves = 0
    
    for i in range(n-1):
        if matchboxes[i] < matches_per_box:
            moves += matches_per_box - matchboxes[i]
            matchboxes[i+1] -= matches_per_box - matchboxes[i]
        elif matchboxes[i] > matches_per_box:
            moves += matchboxes[i] - matches_per_box
            matchboxes[i+1] += matchboxes[i] - matches_per_box
    
    return moves

# Input
n = int(input())
matchboxes = list(map(int, input().split()))

# Output
print(calculate_moves(n, matchboxes))
