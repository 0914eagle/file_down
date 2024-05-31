
def min_moves_to_equalize(n, matchboxes):
    total_matches = sum(matchboxes)
    matches_per_box = total_matches // n
    moves = 0
    for i in range(n-1):
        diff = matchboxes[i] - matches_per_box
        matchboxes[i+1] += diff
        moves += abs(diff)
    return moves

# Input
n = int(input())
matchboxes = list(map(int, input().split()))

# Output
print(min_moves_to_equalize(n, matchboxes))
