
def min_lifting(N, M, initial_state, final_state):
    total_books = sum([1 for shelf in initial_state for book in shelf if book != 0])
    
    initial_positions = {}
    final_positions = {}
    for i in range(N):
        for j in range(M):
            if initial_state[i][j] != 0:
                initial_positions[initial_state[i][j]] = (i, j)
            if final_state[i][j] != 0:
                final_positions[final_state[i][j]] = (i, j)
    
    moves = 0
    for book in range(1, total_books + 1):
        if initial_positions[book] != final_positions[book]:
            initial_i, initial_j = initial_positions[book]
            final_i, final_j = final_positions[book]
            moves += abs(initial_i - final_i) + abs(initial_j - final_j)
    
    return moves // 2 if moves % 2 == 0 else -1

# Input reading
N, M = map(int, input().split())
initial_state = [list(map(int, input().split())) for _ in range(N)]
final_state = [list(map(int, input().split())) for _ in range(N)]

# Output
print(min_lifting(N, M, initial_state, final_state))
