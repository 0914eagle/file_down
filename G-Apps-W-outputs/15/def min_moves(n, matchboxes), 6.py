
def min_moves(n, matchboxes):
    total_matches = sum(matchboxes)
    target_matches = total_matches // n
    moves = 0
    for i in range(n-1):
        diff = target_matches - matchboxes[i]
        matchboxes[i] += diff
        matchboxes[i+1] -= diff
        moves += abs(diff)
    return moves

# Input
n = int(input())
matchboxes = list(map(int, input().split()))

# Output
print(min_moves(n, matchboxes))
