
def minimum_moves(n, matchboxes):
    target_matches = sum(matchboxes) // n
    moves = 0
    for i in range(n):
        diff = target_matches - matchboxes[i]
        if diff > 0:
            moves += diff
            matchboxes[i] += diff
            if i < n - 1:
                matchboxes[i+1] -= diff
    return moves

# Input
n = int(input())
matchboxes = list(map(int, input().split()))

# Output
print(minimum_moves(n, matchboxes))
